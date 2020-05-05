# Занятие 11. Internet, HTTP, REST. PROPERTY 13-17
# Материалы для занятия: https://drive.google.com/file/d/1ZCjk4aaPsMW0nRrWRPiT9wzKhAhKZsey/view
# Видео об Internet, HTTP, REST https://youtu.be/DqCSm70oeT0

import requests                             #Библиотека, работающая с запросами

# res = requests.get("https://python.org")    #Запрос с помощью метода .get
# print(res)                                  #Response [200] - Успешное подтверждение от сайта
# print(dir(res))                             #Методы в объекте res
#
# print()
# print(res.status_code)
#
# print()
# print(res.headers)
#
# print()
# print(res.content)                          #Весь html всей страницы


# Другой пример

# res = requests.get('https://www.python.org/static/img/python-logo@2x.png')      #запрос на картинку

res = requests.get('https://kuna.io/api/v2/depth?market=btcuah')    #запрос на json на биржу биткоина
# print(res.headers['Content-Type'])                                #Информация о типе данный, который к нам вернётся
print(res.json())                                                   #получение json-словаря
print(res.text)                                                     #получение ответа в виде универсального текста, чтоб можно было проанализировать.


# print(res.text)
# print(res.headers['Content-Type'])