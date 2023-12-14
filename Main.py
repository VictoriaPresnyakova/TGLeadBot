from dotenv import load_dotenv
import os
from telebot import TeleBot, types

load_dotenv()
bot=TeleBot(os.getenv('BOT_TOKEN'))


# Обработчик команды /send_circle_video
@bot.message_handler(commands=['start'])
def menu(message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Примеры")
    btn2 = types.KeyboardButton("Менеджер")
    btn3 = types.KeyboardButton("Стоимость услуг")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот компании TGLead".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Менеджер" or message.text == "Купить":
        bot.send_message(message.chat.id,
                         text="Спасибо, чтоб обратились в нашу компанию, мы свяжемся с вами в ближайшее время, если не хотите ждать можете уже сейчас связаться с нашим менеджером: @Maria_Archipovaa")
        bot.send_message(6960800201, f'пользователь @{message.from_user.username} обратился к нам через бот')
    elif message.text == "Стоимость услуг" or message.text == "Пакетные предложения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Купить")
        button2 = types.KeyboardButton("Меню")
        markup.add(button1, button2)
        bot.send_photo(message.chat.id,
                       photo='AgACAgIAAxkBAAMsZXm1sgeFemI450RECwABxEZPsezNAAIz1DEbM2PQSzOZrubLMPvLAQADAgADcwADMwQ',
                       caption='Пакетные предложения', reply_markup=markup)

    elif message.text == "Меню":
        menu(message)

    elif message.text == "Примеры":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        add = types.InlineKeyboardButton(text="Аналитика",
                                         callback_data=str({'param': 'аналитика', 'chat_id': str(message.chat.id)}))
        add1 = types.InlineKeyboardButton(text="Рассылка",
                                          callback_data=str({'param': 'рассылка', 'chat_id': str(message.chat.id)}))
        add2 = types.InlineKeyboardButton(text="Настройка рабочего места",
                                          callback_data=str({'param': 'рабочее', 'chat_id': str(message.chat.id)}))
        add3 = types.InlineKeyboardButton(text="Поиск рекламных каналов",
                                          callback_data=str({'param': 'рекламных', 'chat_id': str(message.chat.id)}))
        add4 = types.InlineKeyboardButton(text="Поиск по ключевым словам",
                                          callback_data=str({'param': 'ключевым', 'chat_id': str(message.chat.id)}))

        keyboard.add(add, add1, add2, add3, add4)
        bot.send_photo(message.chat.id,
                       photo='AgACAgIAAxkBAAOvZXqwjskXdqjB22ffYczIciHB068AArnQMRskOdlLxiVVZcIB1r4BAAMCAANzAAMzBA',
                       reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        data = eval(call.data)
        info = {'аналитика': {'caption': 'Аналитика',
                              'photo': 'AgACAgIAAxkBAAOAZXqoFOeTKXqyvXg5YRBmRAWvIjwAAoXQMRskOdlL-DZOZhbgXGQBAAMCAANzAAMzBA'},
                'рассылка': {'caption': 'Рассылка',
                             'photo': 'AgACAgIAAxkBAAN-ZXqneCXohcPD7FL-Ur4sydgMyt8AAoDQMRskOdlLDi8_ni3OoCQBAAMCAANzAAMzBA'},
                'рабочее': {'caption': 'Настройка рабочего места',
                            'photo': 'AgACAgIAAxkBAAOCZXqoYT4NIdtCG6isVQt7bZ2E9XkAAofQMRskOdlL_Yjiqqk-KDABAAMCAANzAAMzBA'},
                'рекламных': {'caption': 'Поиск рекламных каналов',
                              'photo': 'AgACAgIAAxkBAAOEZXqo-hh26a9ufqxdJkoQfT_aH-kAAozQMRskOdlLFpIxfblatQEBAAMCAANzAAMzBA'},
                'ключевым': {'caption': 'Поиск по ключевым словам',
                             'photo': 'AgACAgIAAxkBAAOGZXqpOjEEMRzr0l-81qkEG1GmXLwAAo_QMRskOdlL6JqQjWECBaUBAAMCAANzAAMzBA'},
                }
        bot.send_photo(int(data['chat_id']), photo=info[data['param']]['photo'], caption=info[data['param']]['caption'])


@bot.message_handler(content_types=["video_note"])
def handle_video_note(message):
    video_note_id = message.video_note.file_id
    print(video_note_id)
    bot.send_message(message.chat.id, video_note_id)
    # bot.send_video_note(chat_id=chat_id,
    # data='DQACAgIAAxkBAAMEZXmTlA0-Ct46NSAIfNJelN0iIpMAAk8_AAJQq8lL9RbmuLPDvhszBA')


@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    photo_id = message.photo[0].file_id
    bot.send_message(message.chat.id, photo_id)


bot.infinity_polling()
