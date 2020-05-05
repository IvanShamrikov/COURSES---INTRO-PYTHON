# Конспект. Занятие 6. ФУНКЦИИ. ИМПОРТЫ Python 13-17




# МНОГОСТРОЧНЫЕ КОММЕНТАРИИ В ФУНКЦИИ
# Делаются с помощью тройных кавычек '''_'''

def bar10(*args, **kwargs):

# ''' Эта функция принимает в себя аргументы из
# места а, а также словари из места b.
# После этого она делает с ними магию.
# И возвращает кролика.
# '''
    print('args-->', args)
    print('kwargs-->', kwargs)

d = {'a': 1, 'b': 2, 'z': 4, 'ddd': 'qwerghj'}
L = [1,2,3,4,5]

bar10(*L, **d)



#
# def foo(a, b, c, **kwargs):
#     """what is bla bla bla
#     :param a: int
#     :param b: float
#     :param c: None
#     :return:  some data
#     """
#     pass



# ---------------------------
#
# ПЕРЕПРИВЯЗКА ИМËН ФУНКЦИЙ
#
# def first (a):
#     print (a)
#
# first ("Hello World")
# second = first
#
# second("Hello World")
#
# -----------------------------
#
# ПЕРЕДАЧА ФУНКЦИИ В ФУНКЦИЮ
#
# def foo (*args):
#     print (args)
#
#
# def foo2 (foo, arg_list):
#     res = foo(*arg_list)
#     return res



# ------------------------------
# РЕКУРСИЯ - ВЫЗОВ ФУНКЦИИ САМУ СЕБЯ
#
# data = {
#     '1': '1',
#     '2': '2',
#     '3': 3,
#     '4': {
#         '5': 1234
#     }
# }
#
# def dict_parser(my_data):
#
#     for i in my_data.items():
#         if not isinstance(i[1], (str, dict)):
#             print('NOT')
#         else:
#             print('YES')
#
#
# def dict_parser1(my_data):
#
#     for i in my_data.items():
#         if not isinstance(i[1], (str, dict)):
#             print(i)
#             print('NOT')
#
#         elif isinstance(i[1], dict):
#             print(i)
#             dict_parser1(i[1])
#
#         else:
#             print(i)
#             print('YES')
#
# ------------------------------------
#
# ПРИМЕР РЕКУРСИИ - ВЫЧИСЛЕНИЕ ЧИСЛА ФИБОНАЧЧИ N-ННОГО ПОРЯДКА
#
# counter = 0         #Счётчик вызовов функции
#
# def fib (n):
#     global counter
#     counter +=1
#     if n == (1,2):
#         return 1
#     else:
#         return fib(n-1) + fib (n-2)
#
# fib (10)      # Попробовать 20, 30
# print(counter)
#


# Решение задачи не через рекурсию.

# counter = 0         #счётчик операций
# def fib2 (n):
#     f1 = 1
#     f2 = 2
#     global counter
#
#     while n > 0:
#         counter +=1
#         f1, f2 = f2, (f1+f2)
#         n -=1
#
#     return f2
#
# print(fib2(30))
# print(counter)

# ---------------------------

# ПОЧЕМУ В ФУНКЦИЮ НУЖНО ПЕРЕДАВАТЬ НЕИЗМЕНЯЕМЫЕ ЗНАЧЕНИЯ?
# d = { '1': 1 }
# def example(data):
#     print('func before-->', data)
#     data['2'] = 2
#     print('func after-->', data)
#
# print('before-->',d)
# d = example(d)            # Без чёткого знания, в какой функции меняется d, мы не сможем отследить, почему произощли изменения.
# print('after-->',d)

# -------------------------





# ИМПОРТЫ -
# Модулем в Python называется любой файл с программой (да-да, все те программы, которые вы писали, можно назвать модулями).
# Каждая программа может импортировать модуль и получить доступ к его классам, функциям и объектам.
# Подключить модуль можно с помощью инструкции import.

import copy     #Импорт стандартного модуля copy
import math     #Импорт стандартного модуля math

# import random as r  #Присвоение модулю псевдонима.
# # print(r.random())
#
# print(dir(r))  #Вызов списка доступных методов модуля random
# print(r.randint.__doc__)    #Вызов аннотации метода randit в модуле random

# from random import randint      # Импорт конкретного метода из всей библиотеки random
# from random import randint as r


# import Lesson6  #Импорт методов из файла в той же папке. Доступно также всё пространство имён этого файла.
# print (dir(Lesson6))
