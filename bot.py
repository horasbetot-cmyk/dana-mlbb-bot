import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN belum diatur. Tambahkan token bot sebagai environment variable BOT_TOKEN.")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Selamat datang di Bot Promo DANA & MLBB! 🎁\n"
        "Gunakan /promo untuk melihat informasi promo."
    )


@bot.message_handler(commands=["promo"])
def promo(message):
    bot.reply_to(
        message,
        "Informasi promo DANA dan MLBB akan diumumkan di sini."
    )


if __name__ == "__main__":
    bot.infinity_polling()
