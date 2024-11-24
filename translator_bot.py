import os
from deep_translator import GoogleTranslator
import telebot
import logging

# Load bot token from environment variable
BOT_TOKEN = '7737706018:AAGQtJNtbqSpwGPlqv70tauuO8pzEywWE5U'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Salom! Matnni yuboring, men uni tarjima qilib beraman.")

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        translated_text = GoogleTranslator(source='auto', target='en').translate(message.text)
        bot.reply_to(message, f"Tarjima:\n{translated_text}")
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {e}")

try:
    bot.infinity_polling()
except Exception as e:
    print(f"Botni ishga tushirishda xato: {e}")
