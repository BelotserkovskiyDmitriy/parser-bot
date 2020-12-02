import telebot

from pars_func import search_title
from config import PAGES


TOKEN = "1401144324:AAF_3J0Aci8KcaI1vK55MGm1bUcrY8Zk340"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_verification(message):
    list_of_content = []
    for page in PAGES:
        list_of_content.extend(search_title(page))
    for data in list_of_content:
        description = data["description"]
        image = data["image"]
        bot.send_message("-1001372573776", f"{description}\n{image}")


bot.polling(none_stop=True)
