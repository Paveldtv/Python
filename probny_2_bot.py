import telebot
from config import TOKEN, keys
from extensions import APIExcetion, Converter
from telebot import types

bot = telebot.TeleBot(TOKEN)
print('Запуск')


#Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    if message.text=='/help':
        text='Формат правильной команды:\n доллар рубль 1'
    else:
        text = 'Что бы конвертировать валюту введите команду в следующем формате:\n ' \
               '<Имя валюты > ' \
               '<Валюта в которую необходимо конвертировать> ' \
               '<Количество валюты>\nСписок доступных валют /values'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/help")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text.format(
                         message.from_user), reply_markup=markup)


# Обрабатываются сообщения, содержащие команду "/values".
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступные валюты: '
    for key in keys.keys():
        text='\n'.join((text,key, ))
    bot.reply_to(message, text)


# Обрабатываются запросы на конвертацию
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    str=message.text.lower()
    values = str.split(' ')
    try:
        if len(values) > 3:
            raise APIExcetion('Слишком много параметров')
        elif len(values) < 3:
            text="{0.first_name} привет! Что бы начать работу выберете команду /start или /help'"
        base, quote, amount = values
        total_base = Converter.get_price(base, quote, amount)
    except APIExcetion as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Неверная команда\n{e}")
        text='Ошибка!'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        btn2 = types.KeyboardButton("/help")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text=text.format(
                             message.from_user), reply_markup=markup)

    else:
        text = f'Стоимость {amount} {base} в {quote} - {round(total_base * int(amount),2)} '
        bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['photo','voice','video','sticker','document'])
def error_types(message):
    bot.reply_to(message, "Неверная команда")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/help")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="{0.first_name} Что бы начать работу выберете команду /start или /help'".format(
                         message.from_user), reply_markup=markup)


bot.polling(none_stop=True)