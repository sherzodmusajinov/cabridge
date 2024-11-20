import logging
from aiogram import Bot, Dispatcher, executor, types
from buttns import menu
from aiogram.types import InputFile


API_TOKEN = '7577184161:AAErUSL2OgVbeZZ7jiRaNboOeiotH0TgNVs'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum IELTS Cambridge kitobni 1-18 tanlang!", reply_markup=menu)

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("Kitob jonatilmoqda ozgincha kutib turing!")

    if message.text == "Camridge 01 📕":
        document = InputFile("Cambridge IELTS 01_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 02 📗":
        document = InputFile("Cambridge IELTS 02_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 03 📔":
        document = InputFile("Cambridge IELTS 03_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 04 📚":
        document = InputFile("Cambridge IELTS 04_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 05 📕":
        document = InputFile("Cambridge IELTS 05_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 06 📗":
        document = InputFile("Cambridge IELTS 06_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 07 📔":
        document = InputFile("Cambridge IELTS 07_compressed_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 08 📚":
        document = InputFile("Cambridge IELTS 08_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 09 📕":
        document = InputFile("Cambridge IELTS 09_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 10 📗":
        document = InputFile("Cambridge IELTS 10_compressed_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 11 📔":
        document = InputFile("Cambridge IELTS 11 AC_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 12 📚":
        document = InputFile("Cambridge IELTS 12 Ac_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 13 📕":
        document = InputFile("Cambridge IELTS 13_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 14 📗":
        document = InputFile("Cambridge IELTS 14_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 15 📔":
        document = InputFile("Cambridge IELTS 15 Ac_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 16 📚":
        document = InputFile("Cambridge IELTS 16 Academic_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 17 📕":
        document = InputFile("IELTS_Cambridge1-Cambridge-IELTS-17_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    elif message.text == "Camridge 18 📗":
        document = InputFile("IELTS_CAMBRIDGE1-IELTS-18-Academic_compressed.pdf")
        await bot.send_document(chat_id=message.chat.id, document=document)

    else:
        await message.reply("Bizning botimizdan foydalanganiz uchun raxmat!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
