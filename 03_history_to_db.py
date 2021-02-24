import sqlite3
from os import getenv

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
KOMMERSANT_CHANNEL_ID = -1001038402501

tg_clone_of_me = Client("me", API_ID, API_HASH)


with tg_clone_of_me as app:
    # Подключаемся к БД (если её нет, она будет создана с нуля)
    con = sqlite3.connect("test.db")
    with con:
        # создаём курсор для обработки результатов запросов к БД
        cur = con.cursor()
        # создаём модель для хранения сообщений из искомого ТГ-канала
        # в модели объявляем 4 поля
        cur.execute(
            "CREATE TABLE IF NOT EXISTS TestMessages(id_сообщения integer PRIMARY KEY, канал TEXT, дата_и_время timestamp, текст TEXT)"
        )
        try:
            # через ТГ-клиент с помощью метода .iter_history
            # достаём 20 последних сообщений
            for message in app.iter_history(
                chat_id=KOMMERSANT_CHANNEL_ID,
                limit=20
            ):
            # и записываем данные из этих сообщений в нашу базу
                cur.execute(
                    "INSERT INTO TestMessages VALUES(?, ?, ?, ?)", (
                        message.message_id,
                        message.chat.title,
                        message.date,
                        message.caption or message.text
                    )
                )
        except sqlite3.IntegrityError:
            pass
