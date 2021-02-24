from dotenv import load_dotenv
from os import getenv
from pyrogram import Client

load_dotenv()

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

# Создадим копию себя для телеграма - создадим своего тг-клиента
# Клиенту мы можем поручать делать всё, что можем сделать сами
tg_clone_of_me = Client("me", API_ID, API_HASH)

# Отправим сами себе два сообщения (они упадут в "Избранное"/Saved Messages)
with tg_clone_of_me as app:
    # используем метод send_message и отправляем первое сообщение
    app.send_message(
        # достаточно указать id ТГ-канала, группы, личного чата
        # для собственных сохранёнок можно указать "me" или "self"
        chat_id="me",
        # плюс нужно указать текст сообщения
        text="Учусь рулить своим телеграмом удалённо"
    )

    # а теперь добавим эмодзи в наше сообщение
    # формат "\N{название эмодзи}"
    # названия эмодзи тут https://apps.timwhitlock.info/emoji/tables/unicode

    # отправляем второе сообщение, теперь уже с эмодзи
    app.send_message(
        chat_id="me",
        text="А вот сообщение с эмодзи \N{victory hand}"
    )
