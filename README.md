# VK Deanonymizer
<a href="https://python.org"><img src="https://img.shields.io/badge/python-3-green.svg" /></a>
## Программа, деанонимизируящая аккаунты VK

# Как это работает?
* Программа анализирует друзей цели и, основываясь на их открытой информации, определяет реальные данные цели.

# Требование к цели
* У цели должно быть больше 20-30 друзей, чтобы гарантировать точность.
* Ее друзья не должны быть скрыты.
* Вы не должны быть в ЧС у цели.

# Установка
## Установка на Linux
```
$ git clone https://github.com/jieggii/vk-deanonymizer.git
$ cd vk-deanonymizer/
$ sudo apt update
$ sudo apt install python3
$ sudo apt install python3-pip
$ sudo pip3 install -r requirements.txt
```

## Установка на Windows
1. Скачайте <a href="https://github.com/jieggii/vk-deanonymizer.git">vk-deanonymizer</a>.
2. Скачайте интерпретатор Python 3 с <a href="https://python.org">официального сайта</a>.
3. Начните установку Python 3.
4. При установке нажмите на кнопку "Customize installation" и убедитесь, что стоит галочка на пункте "pip".
5. Откройте коммандную строку (cmd).
6. Пропишите команду ```cd [путь до vk-deanonymizer]```
7. Пропишите команду ```pip install  -r requirements.txt```

# Запуск
#### Чтобы воспользоваться программой, вам необходимо получить ВК access token. Это можно сделать например <a href="https://vkhost.github.io/">здесь</a>.
* Поместите ваш ВК access token в файл ```key.txt```
## Использование
```vk-deanonymizer [user_id]```
## Примеры
```
vk-deanonymizer 123
vk-deanonymizer 12567
```
# Инфо
* Точность работы программы напрямую зависит от количества друзей цели, и от того, какая информация указана у них в профиле.
* Под заголовком ```Computational information``` будет выведена информация, которая была получена с помощью анализа друзей.
* Под заголовком ```Public information``` будет выведена информация, указанная в профиле цели.


# Предупреждение
* Программа создана исключительно с добрыми намерениями.
* Использование программы в незаконных целях запрещено.
