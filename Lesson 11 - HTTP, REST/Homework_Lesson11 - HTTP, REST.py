# Подключитесь к API НБУ (описание API - https://old.bank.gov.ua/doccatalog/document?id=72819047), получите текущий курс валют и верните в таком виде:
# "дата создания запроса"
# 1 - "название ввалюты1" -- "курс"
# 2 - "название ввалюты2" -- "курс"
# 3 - "название ввалюты3" -- "курс"
# так все валюты, которые придут
#
# 1* Запишите полученные данные в файл в таком же виде
# 2.** Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны к этой валюте за указаную дату используя API НБУ. Формат ввода пользователем данных - на ваше усмотрение. Реализовать с помощью ООП!



# ЗАДАНИЕ 1.
# Запишите полученные данные в файл в таком же виде         #Домашка не сделана, я не понял, как её делать

import requests

class NBU():
    url = None
    kwargs = None
    res = None

    def __init__(self, url, kwargs):
        self.url = url
        self.kwargs = kwargs
        self.res = None

    def request_get(self):
        try:
            self.res = requests.get(self.url)
        except:
            pass

    def pars_resp(self):
        if not self.res:
            return

        if self.res.status_code == 200:
            return self.res.json()
        else:
            # to do smth
            pass

    def prep_answer(self, res):
        if not self.res:
            # to do smth
            pass
        # to do calculation




resultNBU = NBU()
res = requests.get("https://bank.gov.ua/NBU_Exchange/exchange?")
print(res.headers['Content-Type'])

