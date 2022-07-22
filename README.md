# Check_clicks

# Работа с сервисом bit.ly

Программа работы с API сервиса сжатия(укорачивания) ссылок [https://bitly.com](https://bitly.com/a/sign_up).

## Окружение и установка

Python должен быть установлен.

## Установка скрипта

- Скачайте код: [https://github.com/NolongerHumanOrKilua/Check_clicks](https://github.com/NolongerHumanOrKilua/Check_clicks), или клонируйте `git` репозиторий в локальную папку:
```
git clone https://github.com/NolongerHumanOrKilua/Check_clicks
```
- Зарегистрирутесь на сайте [https://bitly.com](https://bitly.com) и получите персональный токен. Токен поместите в файл `.env`:
```
BIT_TOKEN=ваш токен
```

## Запуск

- Запустите программу командой:
```bash
python main.py {url}
```

## Как работает

 Программа `main.py` запрашивает у пользователя адрес ссылки. Анализирует введенную ссылку. В зависимости от введенной ссылки, трансформирует ссылку в сокращённую `bit.ly` ссылку или выводит количество переходов по `bit.ly` ссылке.

## Особенности работы

`main.py` содержит функции:

* Функция `is_bitlink` - проверяет ссылку через API `bit.ly`. Является входящаяя ссылка сокращенной `bit.ly` ссылкой?
* Функция `shorten_link` трансформирует ссылку в сокращённую `bit.ly` ссылку.
* Функция `count_clicks` подсчитывает количество переходов по сокращённой `bit.ly` ссылке.