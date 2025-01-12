#https://t.me/Popov_B2112_bot
from telegram import  Update
from telegram.ext import  ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import  BeautifulSoup


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def virsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Зоре моя вечірняя,...'
                                    f' Зійди над горою,...'
                                    f' Поговорим тихесенько...'
                                    f' В неволі з тобою....'
                                    f' Розкажи, як за горою...'
                                    f' Сонечко сідає,...'
                                    f' Як у Дніпра веселочка Воду позичає....'
                                    f' Як широка сокорина Віти розпустила…...'
                                    f' А над самою водою Верба похилилась;...'
                                    f' Аж по воді розіслала Зеленії віти,...'
                                    f' А на вітах гойдаються Нехрещені діти. {update.effective_user.first_name}')

app = ApplicationBuilder().token("7741194068:AAEZbzGuMWTxBWAI-mvLaQ5m2NGkcxwOF6Q").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()

