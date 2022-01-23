from telegram.ext import *
from datetime import datetime

API_KEY = 'Enter your api key'

print("Bot started...")

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I am CODE Programmer!"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you."

def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('If you need help! You should ask for it on Google!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
