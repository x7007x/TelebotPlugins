import os
import sys
import importlib
import inspect
from telebot import TeleBot
from telebot.async_telebot import AsyncTeleBot
from typing import Union, List, Optional

class TelebotWithPlugins:
    """
    A simple library to add plugins functionality to telebot (pyTelegramBotAPI).
    Allows using the bot without having to define it in each plugin file
    and handles relative paths with respect to the main.py file location.
    """
    
    def __init__(
        self, 
        bot: Union[TeleBot, AsyncTeleBot],
        plugins: str = "plugins",
        exclude: Optional[List[str]] = None,
        main_dir: Optional[str] = None
    ):
        """
        Initialize TelebotWithPlugins
        
        Args:
            bot (TeleBot or AsyncTeleBot): Bot instance from telebot
            plugins (str): Folder containing plugin files (can be dot notation like "source.modules" or path like "source/modules")
            exclude (List[str]): List of filenames to exclude
            main_dir (str): Path to the main directory, if None the main file path will be used
        """
        self.bot = bot
        # Convert dot notation to path if needed
        self.plugins_folder = plugins.replace(".", os.sep) if "." in plugins else plugins
        self.exclude = exclude or []
        
        self.is_async = isinstance(bot, AsyncTeleBot)
        
        if main_dir is None:
            frame = inspect.stack()[1]
            main_dir = os.path.dirname(os.path.abspath(frame.filename))
        self.main_dir = main_dir
        
        if 'telebot' in sys.modules:
            sys.modules['telebot'].bot = self.bot
        
        self._load_plugins()
        
    def _load_plugins(self):
        """Load all plugins from the specified plugins folder"""
        # Convert paths with slashes to system-appropriate format if needed
        self.plugins_folder = self.plugins_folder.replace("/", os.sep)
        
        plugins_path = os.path.join(self.main_dir, self.plugins_folder)
        if not os.path.exists(plugins_path):
            os.makedirs(plugins_path, exist_ok=True)
            # Create an empty __init__.py file
            with open(os.path.join(plugins_path, "__init__.py"), "w") as f:
                pass
            return
        
        # Ensure __init__.py files exist in all directories
        self._ensure_init_files(plugins_path)
        
        if self.main_dir not in sys.path:
            sys.path.insert(0, self.main_dir)
        
        loaded_plugins = 0
        for root, dirs, files in os.walk(plugins_path):
            for file in files:
                if file.endswith(".py") and file != "__init__.py" and file not in self.exclude:
                    rel_path = os.path.relpath(os.path.join(root, file), self.main_dir)
                    module_path = os.path.splitext(rel_path)[0].replace(os.sep, ".")
                    
                    try:
                        importlib.import_module(module_path)
                        loaded_plugins += 1
                    except Exception as e:
                        print(f"Error loading plugin {module_path}: {str(e)}")
    
    def _ensure_init_files(self, root_path):
        """Ensure all directories have __init__.py files for proper importing"""
        # First create an __init__.py in the root plugins directory
        init_path = os.path.join(root_path, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, "w") as f:
                pass
        
        # For dot notation like "source.modules", we need to ensure each part has an __init__.py
        parts = self.plugins_folder.split(os.sep)
        current_path = self.main_dir
        
        for part in parts:
            current_path = os.path.join(current_path, part)
            init_file = os.path.join(current_path, "__init__.py")
            if os.path.isdir(current_path) and not os.path.exists(init_file):
                with open(init_file, "w") as f:
                    pass
