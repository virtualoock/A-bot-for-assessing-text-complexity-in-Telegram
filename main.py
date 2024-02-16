from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from textstat import flesch_kincaid_grade

TOKEN = "YOUR_TOKEN"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для оценки сложности текста. Просто отправь мне текст, и я дам оценку его сложности.')

def analyze_text(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    grade = flesch_kincaid_grade(text)

    update.message.reply_text(f'Оценка сложности текста: {grade}')

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, analyze_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
