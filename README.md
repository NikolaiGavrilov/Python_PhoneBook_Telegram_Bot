# Телеграм бот "Телефонный справочник"
## Информация о проекте
Этот бот служит своего рода телефонной контактной книжкой.
Результаты работы записывает в файл JSON, данные берет оттуда же.

С ботом можно общаться через интерфейс с иконками.
![Визуальный интерфейс бота](instruction.jpg)

Также предусмотрены следующие команды: 
```
/start - запуск бота
/stop - остановка бота
/all - показать все контакты
/add - добавить контакт
/save - сохранить прогресс
/full - узнать всю информацию о контакте, введя его имя
/remove - удалить конткат из справочника
/edit - редактировать информацию о контакте
```

## Инструкции по установке и запуску бота
Предусловия: Должны быть установлены Python с официального сайта python.org и расширение в VS Code для языка Python (его можно найти в Extensions или по [ссылке](https://marketplace.visualstudio.com/items?itemName=ms-python.python)).
Шаги установки:
1. Склонировать себе репозиторий
```
git clone https://github.com/NikolaiGavrilov/Python_PhoneBook_Telegram_Bot
```
2. Перейти в директорию репозитория
```
cd Python_PhoneBook_Telegram_Bot
```
3. Установить telebot
```
pip install telebot
```
4. Установить config
```
pip install config
```
5. Запустить лежащий в репозитории скрипт с ботом
```
python Phonebook_TG_bot.py
```
6. Открыть в Telegram чат с ботом по ссылке [Ссылка на бота](https://t.me/Phone_Book_Gavrilov_bot)
7. Нажать на кнопку СТАРТ/START или ввести команду /start
8. Ознакомиться с присланной ботом инструкцией и начать работу
