import telebot

from config import PAGES, MESSAGE_TEMPLATE
from pars_func import get_flats_info
from db_func import search_by_id, create_connection

TOKEN = "1332879796:AAFmWO753gbbqhPAHQBFfrD-SEvvnjHmkBs"
bot = telebot.TeleBot(TOKEN)
ALLOWED_ID = [434123347, 1001665282]
# channel_id = "-1001277722172"
# my channel
channel_id = "-1001467322816"

post_button = telebot.types.ReplyKeyboardMarkup(True, True)
post_button.row("Опубликовать новые квартиры")


@bot.message_handler(commands=['start'])
def start_verification(message):
    if message.from_user.id in ALLOWED_ID:
        if message.from_user.id == 434123347:
            bot.send_message(message.chat.id, "Доступ разрешен. \nПриветствую, Дмитрий!", reply_markup=post_button)
            bot.send_message(message.chat.id, "Чтобы я нашел нужное обьявление, просто отправьте мне id.", reply_markup=post_button)
        if message.from_user.id == 1001665282:
            bot.send_message(message.chat.id, "Доступ разрешен. \nПриветствую, Сергей!", reply_markup=post_button)
            bot.send_message(message.chat.id, "Чтобы я нашел нужное обьявление, просто отправьте мне id.", reply_markup=post_button)
    else:
        bot.send_message(message.chat.id, "В доступе отказано.")


@bot.message_handler(content_types=['text'])
def process_answers(message):
    if message.from_user.id in ALLOWED_ID and "Опубликовать новые квартиры" in message.text:
        flats_info = []
        for page in PAGES:
            flats_info.extend(get_flats_info(page))
        for info in flats_info:
            post_message = MESSAGE_TEMPLATE.format(object_id=info['object_id'], rooms_count=info['rooms_count'], flat_area=info['flat_area'], flat_floor=info['flat_floor'], total_floors=info['total_floors'], flat_adress=info['flat_adress'], flat_price=info['flat_price'], telegraf_link=info['telegraf_link'])
            bot.send_message(channel_id, post_message)
        bot.send_message(message.chat.id, "Опубликованы новые обьявления", reply_markup=post_button)

    if message.from_user.id in ALLOWED_ID:
        con = create_connection("flats_olx.db")
        link = search_by_id(con, message.text)
        bot.send_message(message.chat.id, link, reply_markup=post_button)


bot.polling(none_stop=True)
