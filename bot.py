
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN belum diatur.")

PROMO_URL = (
    "https://link.dana.id/VAB9W2zV28"
    "?params=[spaceCode=tnc_config_20261029173361202608260094667629173361]"
)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Selamat datang di Bot Promo DANA & MLBB! 🎁\n\n"
        "Perintah tersedia:\n"
        "/promo - Buka informasi promo\n"
        "/buka - Buka halaman promo DANA\n"
        "/status - Cek status bot"
    )


@bot.message_handler(commands=["promo"])
def promo(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            "🎁 BUKA PROMO DANA",
            url=PROMO_URL
        )
    )

    bot.send_message(
        message.chat.id,
        "Promo DANA 11.11\n\n"
        "Gunakan tombol di bawah untuk membuka promo resmi.",
        reply_markup=keyboard
    )


@bot.message_handler(commands=["buka"])
def buka(message):
    bot.reply_to(message, PROMO_URL)


@bot.message_handler(commands=["status"])
def status(message):
    bot.reply_to(
        message,
        "🟢 Bot Telegram aktif.\n"
        "Pemantauan otomatis stok belum diaktifkan."
    )


if __name__ == "__main__":
    print("Bot DANA berjalan...")
    bot.infinity_polling()
