import telebot

BOT_TOKEN = 8230584902:AAGusgIuJWNV1Vrw4yK8yzhFgho7pZq7ks0

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome! XRP Alerts are active.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

print("✅ Bot is running...")
bot.polling()
# --- Keep Replit alive ---
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running"

def run():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()
