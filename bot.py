from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler, CallbackQueryHandler
from commands import start, model, message_handler, gpt, flux
from main import ChatGPT, Flux
import time

context = []

def main():
    application = ApplicationBuilder().token("7911747085:AAGsanmvnE6qdTeteF9XnQ4A8SDq-X2URY0").build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("flux", flux))

    application.add_handler(CommandHandler("gpt", gpt))


    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    application.run_polling()

if __name__ == "__main__":
    main()

