import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

TOKEN = os.environ.get("8734778051:AAEJvCjx2SqUYSli3Ik9cyp8Z9x7p4Zs3Oo")

bot = telebot.TeleBot(TOKEN)

# Flask для keep-alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def get_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("👤 Мій акаунт", url="https://t.me/Favzzet_6542"))
    keyboard.add(InlineKeyboardButton("🌐 Сайт", url="https://pervosatpervosat27-oss.github.io/sitestore2/"))
    keyboard.add(InlineKeyboardButton("💳 Оплата", url="https://send.monobank.ua/jar/87EpSZgx3t"))
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    text = (
        f"Привіт, {name}! 👋\n\n"
        "🏢 *Ласкаво просимо до нашої команди!*\n\n"
        "Ми займаємося:\n"
        "📊 Продажем презентацій на різні теми\n"
        "🤝 Працюємо з великими компаніями\n"
        "🎬 Створюємо прев'ю для відео\n"
        "🌐 Розробкою сайтів\n\n"
        "💼 Якість — наш пріоритет!\n\n"
        "👇 Вибери що тебе цікавить:"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=get_keyboard())

@bot.message_handler(func=lambda m: True)
def any_message(message):
    bot.send_message(message.chat.id, "Скористайся кнопками нижче 👇", reply_markup=get_keyboard())

print("Бот запущено ✅")
Thread(target=run_flask).start()
bot.polling(none_stop=True)