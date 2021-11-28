import telebot
from telebot import types

token = "2103305269:AAHUgFtGDWZfOn4IQ0ZvpXmyfVY8WwlINSQ"
bot = telebot.TeleBot("2103305269:AAHUgFtGDWZfOn4IQ0ZvpXmyfVY8WwlINSQ")

# Создание стартовой команды и выплывающих кнопок
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/Mood", "/reminder", "/info")
    bot.send_message(message.chat.id, 'Привет! Я бот созданный для облегчения ежедневной рутины', reply_markup=keyboard)

# Создание команды /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу помочь тебе отдохнуть: \nФильмы\nКомиксы\n'
                                      'Ютуб\nМузыка\nЕсли что-то заинтересовало, напиши об этом')

# Создание команды /reminder
@bot.message_handler(commands=['reminder'])
def start_message(message):
    bot.send_message(message.chat.id, 'У тебя все обязательно получится!')

# Создание команды /info
@bot.message_handler(commands=['info'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я был создан только для одной цели - уничтожить человечество!(шучу)')


# Создание команды /Оценка бота
@bot.message_handler(commands=['Mood'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Все очень плохо', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Бывало и лучше', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Обычное', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='День удался', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Лучше не бывает!', callback_data=5))
    bot.send_message(message.chat.id, text="Оцените работу бота)", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    if call.data == '1':
        answer = 'Я соболезную'
    elif call.data == '2':
        answer = 'Погуляй с друзьями, точно полегчает'
    elif call.data == '3':
        answer = 'Стабильность!'
    elif call.data == '4':
        answer = 'О, я рад за тебя'
    elif call.data == '5':
        answer = 'Это очень хорошо, наслаждайся моментом'

    # Удаление списка кнопок
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

# Реакции бота на написанный текст
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "Фильмы":
        bot.send_message(message.chat.id, 'Новинки в киноидустрии – https://wink.rt.ru/collections/14')
    if message.text == "Комиксы":
        bot.send_message(message.chat.id, 'Почитать интересные комиксы можешь тут - https://com-x.life/main')
    if message.text == "Ютуб":
        bot.send_message(message.chat.id, 'Если просто хочешь посмотреть видео, то тебе сюда - https://www.youtube.com/')
    if message.text == "Музыка":
        bot.send_message(message.chat.id, 'Здесь классная музыка - https://www.spotify.com/ru-ru/')

# Чтение ботом входящих сообщений пользователя
bot.polling(none_stop=True, interval=0)


