# Обрезка ссылок с помощью Битли
_Используются библиотеки requests, python-dotenv и urllib3_

Программа принимает аргументом в командной строке URL и формирует из него сокращённую ссылку с помощью сервиса bit.ly
Если URL является сокращённой ссылкой bit.ly, то выдаётся количество переходов по этой ссылке.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


Для работы необходима регистрация на сайте bit.ly
В папке с программой нужно создать файл окружения bit.env, куда необходимо поместить строчку с ключом bitly token,
взятую из профиля на сайте bit.ly:
```
BITLY_TOKEN = '<Поместите ваш token сюда>'
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).