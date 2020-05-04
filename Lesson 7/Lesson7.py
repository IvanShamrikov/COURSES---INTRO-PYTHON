# Конспект. Занятие 7. КЛАССЫ. ОБЪЕКТЫ. НАСЛЕДОВАНИЕ Python 13-17

# КЛАСС - инструкция по построению объектов
# Класс может содержать как данные, так и методы их обработки
#
#
# class Car ():     #Как правило, название класса пишется CamelCase методом
#     wheels = 4              #Атрибут класса
#     doors = 5              #Атрибут класса
#
#     def drive(self):   #методы класса - его функции. self - обращение к экземпляру
#         print("Функция foo в объекте Car - ЕХАТЬ!")
#
#
# honda_civic = Car()  #Создаём объект по инструкции (классу) Car
# print(honda_civic)           #Информация об объекте
# print(dir(honda_civic))      #Все методы и аргументы объекта
#
# honda_civic.drive()         #Имеем доступ к методам этого объекта
#
# print(honda_civic.wheels, honda_civic.doors)
# honda_civic.drive()
#
# honda_civic.a = 5     #Перезапись аргумента а в объекте
# print(honda_civic.a)

# print(type(honda_civic))   #Вернёт информацию об объекте, в т.ч. о его классе
# print(honda_civic.__class__)

# ---------------------

# Что такое экземпляр self
#
# class AbcdEfgh ():     #Как правило, название класса пишется CamelCase методом
#     a = 20              #Атрибут класса
#     b = 10              #Атрибут класса
# #1й вариант - не рабочий. Мы просим у функции вывести а, которая не передавалась извне и не создавалась внутри функции.
#     # def foo():
#     #     print("a -- >", a)
# #2й вариант - не рабочий. Мы передали в функцию сам объект, а не переменную а.
#     # def foo(self):
#     #     print("a -- >", a)
# #3й вариант - правильный. Мы в функцию передали объект и вызвали у него .а  Система работает примерно как @ в объектах CodeMonkey
#     def foo(self):
#          print("a -- >", self.a)
#
# first = AbcdEfgh()
# first.foo()




# -----------------------------------


# НАСЛЕДОВАНИЕ

# Без наследования:

# class Car ():
#     wheels = 4
#     doors = 5
#
# class F1Car ():
#     wheels = 4
#     doors = 5
#     nitro = 1000



# С наследованием
#
# class Car ():
#     wheels = 4
#     doors = 5
#     def drive(self):
#         print("Едем")
#
# class F1Car(Car):
#     nitro = 1000
#     def fly(self):
#         print("летим")
#
# print(dir(F1Car))    #В класс F1Car передались все аргументы и методы класса Car
#
# honda_civic = Car()
# print(honda_civic.wheels, honda_civic.doors)
# honda_civic.drive
#
# bolid1 = F1Car()
# print(bolid1.wheels, bolid1.doors, bolid1.nitro)  #В объект bolid1 передались все аргументы и метожа из класса F1Car и класса Car
# bolid1.drive()  #Можно вызвать функцию из материнского класса Car
# bolid1.fly()    #Можно вызвать функцию собственного класса F1Car

# Как узнать, кто кому родитель?
# print(isinstance(honda_civic, Car)) #Вернёт True, при чём по отношению родительского класса любого уровня вложенности


# -------------------
# Переопределение
#
# class Car ():
#     wheels = 4
#     doors = 5
#     def drive(self):
#         print("Едем")
#
# class CoupeCabriolet(Car):
#     doors = 3
#     roof = "removable"
#
#     def drive(self):
#         print ("Едем с ветерком")
#
#
# nissan_coupe = CoupeCabriolet()
# print(nissan_coupe.wheels, nissan_coupe.doors, nissan_coupe.roof, nissan_coupe.drive())


# -------------------------------
#
# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
#
# class TransformerOne():
#     hit = 100
#     defense = 200
#     rockets = 10
#
#     def ulta_transformer_one(self):
#         print("Шквал ракет")
#
# class TransformerTwo():
#     hit = 50
#     defense = 300
#     fireballs = 10
#
#     def ulta_transformer_two(self):
#         print("Стена огня")
#
#
# class MegaTransformer (TransformerOne, TransformerTwo):   #МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
#     hit = 200
#     defense = 500
#
#
# mega1 = MegaTransformer()
# print(dir(mega1))                       #Наследовал все методы и аргументы всех родитиелей
#
# print(isinstance(mega1, TransformerOne))
# print(isinstance(mega1, TransformerTwo))
# print(type(mega1))
# print(mega1.__class__)






