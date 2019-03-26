from telegram.ext import (updater, commandHandler)
updater = updater("846737116:AAHmBvJKd6VFaBlqo_JXiIuB_jJyrFet5aE")

def start_method(bot,update):
    bot.sendmessage(update.message.chat_id, "coded by @reven0")
start_command = CommandHandler('start', start_method)
updater.dispatcher.add_handler(start_command)
