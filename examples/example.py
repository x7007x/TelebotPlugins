from telebot import TeleBot
from telebot_plugins import TelebotWithPlugins

API_TOKEN = "YOUR_BOT_TOKEN"
bot = TeleBot(API_TOKEN)

plugins = TelebotWithPlugins(
    bot=bot,
    plugins="plugins",
    exclude=["disabled_plugin.py"]
)

if __name__ == '__main__':
    bot.polling()
