import telebot

from pars_func import search_title
from config import PAGES


TOKEN = "1472296297:AAErAgInhWiTAvu_9B84jPuaBGL9miI39dM"
bot = telebot.TeleBot(TOKEN)
ALLOWED_ID = [434123347, 1001665282]
channel_id = "-1001277722172"


@bot.message_handler(commands=['start'])
def start_verification(message):
    if message.from_user.id in ALLOWED_ID:
        list_of_content = []
        for page in PAGES:
            list_of_content.extend(search_title(page))
        for data in list_of_content:
            description = data["description"]
            image = data["image"]
            bot.send_message(channel_id, f"{description}\n{image}")


bot.polling(none_stop=True)
