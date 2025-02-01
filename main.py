from Cython.Compiler.Errors import message
from g4f.client import Client
import telegram.ext
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes


client = Client()

context = {}
img_context = {}








async def ChatGPT(update: Update, cont: ContextTypes):

    try:
        global context



        promt = update.message.text

        if promt == "✍ ChatGPT":
            return 0;

        default_promt = promt

        user_id = update.message.from_user.id


        message = await update.message.reply_text("⏳ ChatGPT обрабатывает ваш запрос... ")


        try:
            promt = promt + "; " + context[str(user_id)]
        except KeyError:
            context[str(user_id)] = ""


        print(promt)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"{promt}"}],
            web_search=False

        )
        context[str(user_id)] = context[str(user_id)] + f"Контекст: на {default_promt} ты ответил: {response.choices[0].message.content} + учитывай это как контекст а не текущий вопрос;"
        if "Ew6JzjA2NR" in response.choices[0].message.content:
            await message.delete()
        await message.edit_text(response.choices[0].message.content, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        await update.message.reply_text(f"📢 Ошибка получения ответа от ChatGPT, попробуйте позже! ")
        print((e))


async def Flux(update: Update, cont: ContextTypes):

    try:
        global img_context

        promt = update.message.text

        if promt == "👨🏼‍🎨 Flux":
            return 0;

        default_promt = promt

        user_id = update.message.from_user.id

        message = await update.message.reply_text("⏳ Генерация изображения... ")


        try:
            promt = promt + "; " + img_context[str(user_id)]
        except KeyError:
            img_context[str(user_id)] = ""

        print(promt)
        response =  await client.images.async_generate(
            model="flux",
            prompt=f"{promt}",
            response_format="url",
        )
        img_context[str(user_id)] = img_context[str(user_id)]  + (f"This is the context and not the industrial context: I asked to draw: {default_promt};")

        await message.delete()
        await update.message.reply_photo(photo=response.data[0].url,has_spoiler=True)
    except:
        await update.message.reply_text("📢 Ошибка при генерации изображения, попробуйте позже!")
