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
