# Занятие 11. ОСНОВЫ ООП. АБСТРАКЦИЯ. PROPERTY 13-17

# Самостоятельная работа - напишите программу, которая помогает хозяйке посчитать, сколько ей нужно взять приправ (соль, перец) для заданного количества мяса:
# (соль - 15г на 1 кг мяса, перец - 5 г на 1 кг мяса).
# Время выполнения - 15 минут.
#
# ------
# 15 минут
# ------
#
# Пропорция для соли
# 1000 : 15 = m : x

# def salt_mass(m):
#     return m * 15 / 1000
#
# def pepper_mass(m):
#     return m * 5 / 1000
#
# m = int(input("Введите массу мяса (г) ---> "))
# print(salt_mass(2500), pepper_mass(2500))
#
#
# # Простая абстракция - пример с ингридиентами для мяса (https://youtu.be/BAAZCHEVxUY)
#
# ingredients = {"salt" : 15, "pepper": 5}
#
# def get_ingredients (m, key):
#     return m * ingredients[key] /1000               #Простая абстракция - мы не используем никаких конкретных данных. всё описано обстрактно.
#
# meat = int(input("Введите массу мяса (г) ---> "))
# ing = input("Введите название нужного ингридиента(salt, pepper) ---> ")
# print(get_ingredients(m = meat, key = ing))


















# ЧТО ТАКОЕ АБСТРАКЦИЯ?
# Посмотреть видео перед уроком: https://youtu.be/jq-UlNmHYAQ
# Задать вопрос: Видели ли вы когда-либо мебель? А хотите я Вам докажу, что Вы никогда не видели мебель?
# Нарисовать Мебель->Стул, Мебель->Стол, Мебель->Кровать
# Мебель - абстрактное обобщение конкретного предмета.
#
# Нарисовать схему из видео и пояснить за принцип абстракции метода сборки

# Есть родительский класс и дочерние.
# Мы хотим создать функцию, вычисляющую площадь фигуры. Но формула для разных фигур разная.
#
#---
# Можно реализовать функции в каждом объекте. Но если объектов тьма-тьмущая - можно забыть или ошибиться.

# class Figure():
#     pass
#
# class Circle(Figure):
#     def area(self):
#         print ("Calculating Area")
#
# class Triangle(Figure):
#     def area(self):
#         print("Calculating Area")
#
# class Square ():
#     pass                #забыли прописать функцию. "На проблему напали"
#---

#А можно сделать абстрактный метод, который перенаправляет в конкретный в нужном объекте.

# import abc                          #Библиотека абстрактного класса
#
# class Figure(abc.ABC):              #Наследование абстрактного класса abc.ABC
#     def area(self):
#         print ("Funcion area")
#         return self._area()
#
#     @abc.abstractmethod             #Декоратор, указывающий на абстрактный метод
#     def _area (self):
#         pass
#
#
#
# class Circle(Figure):
#     def _area(self):
#         print("Calculating Area")
#
# class Triangle(Figure):
#     def _area(self):
#         print("Calculating Area")
#
# class Square(Figure):
#     pass
#
# triangle = Triangle()
# triangle.area()
# triangle._area()
#
# square = Square()               #Создание объекта сломается, потому что в классе Square(Figure) конкретно не прописан абстрактный метод его родителя.





# Следующий пример абстракции - получение информации об аргументах из метода

class Metal():
    x = 10
    y = 20

    def __init__(self, a, b):
        self.x = a
        self.y = b

    @classmethod
    def get_x_class(cls):
        return cls.x

    @classmethod                    # Этот декоратор позволяет получать аргументы класса, даже абстрактного. Например, дефолтные значения.
    def get_y_class(cls):
        return cls.y

class Splav1(Metal):
    pass

obj1 = Splav1(100, 200)
print("Показатели сплава", obj1.x, obj1.y)
print("Показатели базового металла", obj1.get_x_class(), obj1.get_y_class())