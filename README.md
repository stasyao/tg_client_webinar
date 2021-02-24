# Учимся работать с телеграм-клиентом на базе python-библиотеки pyrogram

## Инструкция по запуску на своей машине

1. Клонируйте репозиторий `git clone https://github.com/stasyao/tg_client_webinar`
2. Установите в директории проекта и разверните виртуальное окружение
- `python -m venv venv` (в директории проекта появится папка venv)
- `source venv/Scripts/activate` (в терминале над строкой для ввода команд появится обозначение (venv) - значит, виртуальное окружение активировано)
- `pip install -r requirements.txt` (установятся все необходимые библиотеки)
3. Создайте своё телеграмм-приложение и получите его id и hash. Как это сделать, [описано тут](https://docs.google.com/document/d/1RvfjtGdEA-M_nz9v1RRCL2VNeC1fCg4SgmuFoD1BZ4I/edit?usp=sharing).
4. Создайте в директории проекта файл .env. В нем нужно прописать две строки:
- первая строка: API_ID=
- вторая строка: API_HASH= 

После знака = указывается соответственно id и hash без кавычек.

5. Запустите любой python-файл из проекта. В терминале появится предложение ввести номер телефона и подтверждающий код (он придет в ваш телеграм). Введите необходимые данные. Больше они запрашиваться не будут.

```
$ python 02_get_history.py
TgCrypto is missing! Pyrogram will work the same, but at a much slower speed. More info: https://docs.pyrogram.org/topics/tgcrypto
Pyrogram v1.1.13, Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
Licensed under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+)

Enter phone number or bot token: 89969109297
Is "89969109297" correct? (y/N): y
The confirmation code has been sent via Telegram app
Enter confirmation code: 53691
```

6. Обратите внимание на комментарии в коде python-файлов. Они помогут разобраться с тем, как всё устроено.
