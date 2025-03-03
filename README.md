# TeleBot Plugins

A simple plugin system for pyTelegramBotAPI (telebot) that allows you to organize your bot's functionality into separate plugin files without having to redefine the bot instance in each file.

## Features

- Load plugins from a specified directory
- Support for both synchronous and asynchronous telebot
- Handle relative paths properly
- Automatically register the bot instance globally
- Support for webhook and polling modes

## Installation

```bash
pip install telebot-plugins
```

## Usage

### Basic Example

```python
from telebot import TeleBot
from telebot_plugins import TelebotWithPlugins

# Create a bot instance
API_TOKEN = "YOUR_BOT_TOKEN"
bot = TeleBot(API_TOKEN)

# Initialize TelebotWithPlugins
plugins = TelebotWithPlugins(
    bot=bot,
    plugins="plugins",  # plugins folder name
    exclude=["disabled_plugin.py"]  # files to exclude (optional)
)

if __name__ == '__main__':
    # Start the bot
    bot.polling()
```

### Example Plugin File (plugins/example.py)

```python
from telebot import bot  # The bot is automatically available

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! This is a plugin example.")
```

### Async Bot Example

```python
from telebot.async_telebot import AsyncTeleBot
from telebot_plugins import TelebotWithPlugins
import asyncio

# Create an async bot instance
API_TOKEN = "YOUR_BOT_TOKEN"
bot = AsyncTeleBot(API_TOKEN)

# Initialize TelebotWithPlugins
plugins = TelebotWithPlugins(
    bot=bot,
    plugins="plugins"
)

if __name__ == '__main__':
    # Start the async bot
    asyncio.run(bot.polling())
```
