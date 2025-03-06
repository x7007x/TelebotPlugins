from telebot import types

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello! This is an example plugin.")

@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.reply_to(message, "This bot supports plugins.")
