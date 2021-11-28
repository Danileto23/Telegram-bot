import telebot
from telebot import types

token = "2138712685:AAEeyqtUby3uksS2BSln5S1tRiEgYaIFPGI"
bot = telebot.TeleBot("2138712685:AAEeyqtUby3uksS2BSln5S1tRiEgYaIFPGI")

# Создание стартовой команды и выплывающих кнопок
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Личный кабинет", "/help", "/grade_bot", "/reminder", "/info")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

# Создание команды /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу помочь тебе с информацией о МТУСИ: \nЛичный кабинет\nНовости\n'
                                      'Расписание\nО МТУСИ\nЕсли что-то заинтересовало, напиши об этом')

# Создание команды /reminder
@bot.message_handler(commands=['reminder'])
def start_message(message):
    bot.send_message(message.chat.id, 'У тебя все обязательно получится!')

# Создание команды /info
@bot.message_handler(commands=['info'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я был создан только для одной цели - уничтожить человечество(шучу)'
                                      'Кстати, можешь оставь свой отзыв тут - /grade_bot\nСпасибо')

# Создание команды /grade_bot
@bot.message_handler(commands=['grade_bot'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Никуда не годится', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Старайся лучше', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Нууу, сойдет', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Уже неплохо', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Лучше уже некуда', callback_data=5))
    bot.send_message(message.chat.id, text="Оцените работу бота)", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за ответ')
    answer = ''
    if call.data == '1':
        answer = 'Я разочарован'
    elif call.data == '2':
        answer = 'Делаю все, что в моих силах'
    elif call.data == '3':
        answer = 'Да, сойдет'
    elif call.data == '4':
        answer = 'Я рад'
    elif call.data == '5':
        answer = 'Это превосходно'

# Удаление списка кнопок
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

# Реакции бота на написанный текст
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "Новости":
        bot.send_message(message.chat.id, 'Свежие новости вуза – https://mtuci.ru/about_the_university/news/')
    if message.text == "Расписание":
        bot.send_message(message.chat.id, 'Расписание для всех - https://mtuci.ru/time-table/')
    if message.text == "Личный кабинет":
        bot.send_message(message.chat.id, 'Если учишься в МТУСИ, Welcome - http://room.mtuci.ru')
    if message.text == "О МТУСИ":
        bot.send_message(message.chat.id, 'Сведение об образовательной организации - https://mtuci.ru/sveden/')

# Чтение ботом входящих сообщений пользователя
bot.polling(none_stop=True, interval=0)


