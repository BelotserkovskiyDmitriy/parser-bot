import telebot

TOKEN = "1472296297:AAErAgInhWiTAvu_9B84jPuaBGL9miI39dM"
bot = telebot.TeleBot(TOKEN)
dmitry_id = "434123347"
sergey_id = "1001665282"
channel_id = "-1001277722172"


@bot.channel_post_handler(content_types="text")
def print_data2(message):
    print(message)


@bot.message_handler(commands=['start'])
def print_data(message):
    print(message)


@bot.message_handler(content_types="text")
def print_data3(message):
    print(message)


bot.polling(none_stop=True)
