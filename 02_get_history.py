from os import getenv

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

tg_clone_of_me = Client("me", API_ID, API_HASH)


with tg_clone_of_me as app:
    # https://docs.pyrogram.org/api/methods/get_history
    # возьмём последнее собщение из нашего "Избранного"
    list_of_messages = app.get_history(
        chat_id="me",  # укажем, из какого чата брать
        limit=1  # берем только одно (=последнее) сообщение
        # если limit не указать, получим список из 100 последних сообщений
    )

    # get_history всегда возвращает список, даже если запросили одно сообщение
    # поэтому вытащим его по индексу
    last_message = list_of_messages[0]

    # дальше описываем, что мы хотим сделать с этими сообщениями

    # вывести в консоль только текст сообщения
    print(last_message.text)
    # вывести в консоль текст сообщения и его уникальный номер (id)
    print(last_message.message_id, last_message.text)
    # или отредактировать наше сообщение прямо в телеграме
    # ведь мы знаем его уникальный номер и у нас есть на это права
    # https://docs.pyrogram.org/api/methods/edit_message_text
    app.edit_message_text(
        chat_id="me",
        message_id=last_message.message_id,
        text=f"{last_message.text}...Добавил что-то новое"
    )
    # теперь посмотрите на последнее сообщение в "Избранном"
    # у него должен быть статус "edited"

    # об атрибутах объекта message можно прочитать здесь
    # https://docs.pyrogram.org/api/types/Message#pyrogram.types.Message
