from telegram import Update, ReplyKeyboardMarkup
import time
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler, CallbackQueryHandler

from main import ChatGPT, Flux

model = {}
user_id = 0

async def gpt(update: Update, context: ContextTypes):
    global model, user_id
    await update.message.delete()
    model[str(user_id)] = "ChatGPT"
    await update.message.reply_text("Вы успешно выбрали ChatGPT ✍")

async def flux(update: Update, context: ContextTypes):
    global model
    model[str(user_id)] = "ChatGPT"
    await update.message.delete()
    model = "Flux"
    await update.message.reply_text("Вы успешно выбрали Flux 👨🏼‍🎨")
async def start(update: Update, context: ContextTypes):

    keyboard = [
        ['✍ ChatGPT', '👨🏼‍🎨 Flux'],

    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_text("Привет, я GPT-4o mini и я могу: \n\n› 👨🏼‍🎨 Cоздавать фото по описанию;\n› ✍ Быть вашим текстовым ассистентом.\n\n🤖 Доступные команды: \n\n/gpt - ChatGPT для учебы и работы\n\n/flux - Нейросеть для генерации изображений Flux", reply_markup=reply_markup)



async def message_handler(update: Update, context: ContextTypes):

    global model, user_id

    user_id = update.message.from_user.id

    if update.message.text == "✍ ChatGPT":
        await update.message.delete()
        model[str(user_id)] = "ChatGPT"
        await update.message.reply_text("Вы успешно выбрали ChatGPT ✍")
    elif update.message.text == "👨🏼‍🎨 Flux":
       await update.message.delete()
       model[str(user_id)] = "Flux"
       await update.message.reply_text("Вы успешно выбрали Flux 👨🏼‍🎨")

    if model[str(user_id)] == "ChatGPT":
        await ChatGPT(update,context)
    elif model[str(user_id)] == "Flux":
        await Flux(update, context)