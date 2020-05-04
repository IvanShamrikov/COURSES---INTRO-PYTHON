# Конспект. Занятие 8. ОСНОВЫ ООП. __init__. ДЕКОРАТОРЫ. ГЕТТЕРЫ/СЕТТЕРЫ. PROPERTY 13-17


# -----------------------------
#
# ИНИЦИАЛИЗАЦИЯ АРГУМЕНТОВ ОБЪЕКТА - метод .__init__

# class Car():
#     wheels = 4
#     doors = 5
#     color = None
#
#     def __init__(self, tsvet):
#         self.color = tsvet
#
#
# hiunday_gets = Car ("blue")
# print(hiunday_gets.color)



#
# # Второй случай - приём множественных параметров автомобиля
#
# class Car():
#     wheels = 4
#     doors = 5
#     color = None
#
#
#     def __init__(self, tsvet, kolesa, dveri):
#         self.color = tsvet
#         self.wheels = kolesa
#         self.doors = dveri
#
# hiunday_elantra = Car ("red", 5, 2)
# print(hiunday_elantra.color, hiunday_elantra.wheels, hiunday_elantra.doors)



# -----------------------------
#

# ГЕТТЕРЫ И СЕТТЕРЫ
#
# Применение №1
# В простом исполнении геттеры и сеттеры - это "прокладка" в процессе записывания и доставания информации. В эту прокладку можно
# запрограммировать дополнительный функционал для этапов записи информации в объект или вызова информации из него.

#
# class Car():
#     wheels = 4
#     doors = 5
#     color = None                # Поля color и orderstatus будут записываться и доставаться разными способами - напрямую и через геттер/сеттер.
#     orderstatus = None
# #
#     def __init__ (self,a,b):
#         self.color = a              #Поле color записывается напрямую
#         self.orderstatus_setter(b)  #Поле orderstatus записывается через прокладку-сеттер, в которой выполняется дополнительный функционал.
#
#     # Приём 1
#     def orderstatus_getter(self):
#         print("У программы запросили статус заказа")
#         return self.orderstatus
#
#     def orderstatus_setter(self, status):
#         print("Отправить сообщение директору, что изменили статус заказа")
#         self.orderstatus = status           # Вот тут устанавливается аргумент вместе с выполнением дополнительных команд (тут делается print(...))
#
#
#
# mersedes600 = Car("blue", "На этапе сборки руля")   #Цвет установится в аргумент color напрямую, а статус пройдёт через геттер и только потом запишется в аргумент orderstatus
#
# print(mersedes600.wheels,
#       mersedes600.doors,
#       mersedes600.color,
#       mersedes600.orderstatus)
#
# print(mersedes600.orderstatus)              #Обращение к аргументу напрямую
# print(mersedes600.orderstatus_getter())     #Обращение к аргументу через геттер
#

# -----------------------------
#

# ДЕКОРАТОРЫ
# Метод @decorator - обёртывание выполнения любой функции в какую-то логику.


# def my_decorator(func):
#
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     return wrapper
#
# @my_decorator       # Заменяет my_decorator(foo())
# def foo():
#     print('in foo')
#
# foo()



# Пример декоратора
# Написать декоратор, который бы добавлял длительность введения ответа на вопрос.

# import time
#
# def decorator (foo):
#
#     def wrapper():
#         start = time.time()
#         x = foo()
#         stop = time.time()
#         print ("Ты написал строку ", x, " за ", stop-start, " секунд")
#         return x
#
#     return wrapper
#
# @decorator
# def question():
#     return input("Введи свою Фамилию, Имя и Отчество ---> ")
#
# question()

# # ------------------------
#
# МЕТОД PROPERTY
# Это соединение темы __init__ и Декораторов.
# При записи данных в параметры класса метод PROPERTY позволяет создавать промежуточное значение, в котором спрятаны геттеры и сеттеры.

# ЗАДАНИЕ
    # Создать класс Car с параметрами wheel, doors, color . В класс добавить метод __init__ для всех полей.
    # Применить для всех полей сеттеры, которые проверяют на соответствие тип введённых
    # Добавить для всех полей геттеры, которые считают количество обращений к этому объекту.
    # Инкапсулировать аргументы класса Car с помощью property


# class Car():
#     counter = 0
#     _wheels = None                                  #Создаются поля класса через _ , которые будут наполняться с помощью сеттеров
#     _doors = None
#     _color = None
#
#
#     def __init__(self, a, b, c):            #Принимаются аргументы a,b,c при создании объекта и распределяются по промежуточным переменным(аргументам)
#         self.wheels = a                     # Аргумент wheels - это не просто аргумент. В нём скрыты 2 функции - геттер и сеттер.
#                                                 # Детальнее эта скрытость программируется ниже с помощью функции propetries
#                                                 # В данном случае (__init__) речь идёт о записи информации - Аргумент wheels принимает в
#                                                 # себя значение и вызывает внутри себя сеттер, который перезаписывает наш аргумент _wheels
#         self.doors = b
#         self.color = c
#
#     def set_wheels(self, arg):
#         self._wheels = None
#         if not isinstance(arg, int):
#             print("Введено не число")
#             raise TypeError
#         self._wheels = arg
#
#     def get_wheels(self):
#         self.counter += 1
#         return self._wheels
#
#     def set_doors(self, doors):
#         if not isinstance(doors, int):
#             print("Введено не число")
#             raise TypeError
#         self._doors = doors
#
#     def get_doors(self):
#         self.counter += 1
#         return self._doors
#
#     def set_color(self, color):
#         if not color.lower() in ("blue", "red", "black", "yellow", "green"):
#             print("Нет такого цвета")
#             raise KeyError
#         self._color = color
#
#     def get_color(self):
#         self.counter += 1
#         return self._color
#
#     wheels = property(get_wheels, set_wheels)
#     doors = property (get_doors, set_doors)
#     color = property (get_color, set_color)
#
#
# renault_logan = Car(5, 10, "blue")
#
# print(dir(renault_logan))
# print(renault_logan.wheels,
#       renault_logan.doors,
#       renault_logan.color,
#       renault_logan.counter)
# print("-------------")
# renault_logan.color = "blue"
#
# print(renault_logan.wheels)
# print(renault_logan._wheels)




# -----
# ПРИМЕР ПРИМЕНЕНИЯ МЕТОДА PROPERTY #2
# Создайте родительский класс Transport с аргументами brand и model
# Создайте дочерние классы Car(), Plane(), Moto() c аргументами wheels, passengers.
# Создайте в классах проверку на запись в аргументы:
# Car():
#     - Возможное количество пассажиров Car() - от 2х до 7х
#     - Возможное количество колёс Car() - только 4
# Moto():
#     - Возможное количество пассажиров Moto() - от 2х до 3х
#     - Возможное количество колёс Moto() - от 2х до 3х
# Plane()
#     - Возможное количество пассажиров Plane() - от 2х до 165ти
#     - Возможное количество колёс Plane() - только 3

#
# class Transport():
#     brand = None
#     model = None
#
#
# class Car(Transport):
#     _wheels = None
#     _passengers = None
#
#     def __init__(self, brand = None, model = None, wheels = None, passengers = None):
#         self.brand = brand
#         self.model = model
#         self.wheels = wheels
#         self.passengers = passengers
#
#     def set_wheels(self, wheels):
#         if wheels != 4:
#             print("Вы указали неправильное количество колёс.")
#             raise ValueError
#         self._wheels = wheels
#
#     def get_wheels(self):
#         return self._wheels
#
#     def set_passengers(self, passengers):
#         if passengers <2 or passengers > 7 :
#             print("Вы указали неправильное количество пассажиров.")
#             raise ValueError
#         self._passengers = passengers
#
#     def get_passengers(self):
#         return self._passengers
#
#     wheels = property (get_wheels, set_wheels)
#     passengers = property (get_passengers, set_passengers)
#
#
#
# class Moto(Transport):
#     _wheels = None
#     _passengers = None
#
#     def __init__(self, brand = None, model = None, wheels = None, passengers = None):
#         self.brand = brand
#         self.model = model
#         self.wheels = wheels
#         self.passengers = passengers
#
#     def set_wheels(self, wheels):
#         if wheels < 2 or wheels > 3:
#             print("Вы указали неправильное количество колёс.")
#             raise ValueError
#         self._wheels = wheels
#
#     def get_wheels(self):
#         return self._wheels
#
#     def set_passengers(self, passengers):
#         if passengers < 2 or passengers > 3 :
#             print("Вы указали неправильное количество пассажиров.")
#             raise ValueError
#         self._passengers = passengers
#
#     def get_passengers(self):
#         return self._passengers
#
#     wheels = property (get_wheels, set_wheels)
#     passengers = property (get_passengers, set_passengers)
#
#
# class Plane(Transport):
#     _wheels = None
#     _passengers = None
#
#     def __init__(self, brand = None, model = None, wheels = None, passengers = None):
#         self.brand = brand
#         self.model = model
#         self.wheels = wheels
#         self.passengers = passengers
#
#     def set_wheels(self, wheels):
#         if wheels != 3:
#             print("Вы указали неправильное количество колёс.")
#             raise ValueError
#         self._wheels = wheels
#
#     def get_wheels(self):
#         return self._wheels
#
#     def set_passengers(self, passengers):
#         if passengers <2 or passengers > 165 :
#             print("Вы указали неправильное количество пассажиров.")
#             raise ValueError
#         self._passengers = passengers
#
#     def get_passengers(self):
#         return self._passengers
#
#     wheels = property (get_wheels, set_wheels)
#     passengers = property (get_passengers, set_passengers)
#
# car = Car ("Audi", "TT", 4, 2)
# print(car.brand,
#       car.model,
#       car.wheels,
#       car.passengers)
#
# moto = Moto ("ИЖ","420", 3, 3)
# print(moto.brand,
#       moto.model,
#       moto.wheels,
#       moto.passengers)
#
# plane = Plane ("Boeing","Cargo", 3, 149)
# print(plane.brand,
#       plane.model,
#       plane.wheels,
#       plane.passengers)
#
#
#






# -----------------------------
#
#
# Метод __slots__  - указывает жесткие ограничения по количеству и именам аргументов класса
#
# class Car():
#     __slots__ = ["wheels", "doors", "color"]
#     pass
#
# nissan_juke = Car()
# nissan_juke.wheels = 5
# nissan_juke.doors = 5
# nissan_juke.color = None
#
# # nissan_juke.antena = "yes"
# # print(nissan_juke.antena)
#
# print(dir(nissan_juke))




# -----------------------------

# Метод __str__ - строковое отображение объекта

# class Car():
#     brand = None
#     model = None
#     year = None
#
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
#
#
# nissan_juke = Car(year = 2015, model = "Juke", brand = "Nissan")
# print(nissan_juke.__str__())                                            #Вызов метода




# -----------------------------

# Метод __ad__ - возвращает результат сложения объекта с другим объектом.
# Сейчас мы с помощью сложения 2х мотоциклов получим 1 автомобиль)))

# class Car():
#     brand = None
#     model = None
#
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
#
#
# class MOTO():
#     brand = None
#     model = None
#
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def __add__(self, other):
#         if type(self) == type(other):
#             return Car(brand = self.brand + other.brand, model = self.model + other.model, year = self.year - other.year)
#
#
#
# yamaha_r2 = MOTO(model = "R2", brand = "Yamaha", year = 2015)
# ktm_enduro = MOTO(year = 2019, model = "Enduro", brand = "KTM")
#
# car_frankinstein = yamaha_r2 + ktm_enduro       # При сложении двух объектов программа пойдёт в первый из объектов и будет искать в нём метод .__add__.
#                                                 #Если найдёт - засунет его в параметр функции self, а второй - в параметр other.
# print(type(car_frankinstein))
# print(car_frankinstein.__str__())