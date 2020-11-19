mport telebot
import config

bot = telebot.TeleBot(config.token)

#декоратор приветсвия
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
    "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы повторять за тобой.".format(
                         message.from_user, bot.get_me()), parse_mode='html')

#декоратор дублирования сообщений
@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

#запуск бота
bot.polling(none_stop=True)
