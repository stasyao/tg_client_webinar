from os import getenv

from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

tg_clone_of_me = Client("me", API_ID, API_HASH)

# Создаём хендлер, реагирующий на сообщения: отправку, получение и т.д.
# Сразу задаём фильтр: в обработку будут попадать только saved messages
@tg_clone_of_me.on_message(filters.chat("me"))
def get_chanhels_info(tg_clone_of_me, message):
    channel_info = (
        f"**Название канала**: {message.forward_from_chat.title}\n"
        f"**Username**: @{message.forward_from_chat.username}\n"
        f"**Id канала**: {message.forward_from_chat.id}\n"
    )
    
    tg_clone_of_me.send_message(
        chat_id="me",
        text=channel_info
    )

# Клиент запускается и работает до принудительной остановки
tg_clone_of_me.run()
