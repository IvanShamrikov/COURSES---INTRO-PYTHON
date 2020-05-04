#1. Напишите класс, отвечающий за животное. Реализуйте в классе атрибуты : количество лап, издаваемый звук, кличка.
    # Реализуйте в классе метод "издать звук". Количество лап и звук задается при инициализации и имеет ограничения (ограничения придумайте сами).
    # Кличка дается после инициализции. Создайте несколько обьектов класса, напр кошка, собака, птица, и тд.

#2. Напишите декоратор, который бы сообщал время запуска и время завершения функции.
    # (узнать текущее время можно с помощью модуля time или datetime)

#3. * Реализуйте в классе животное возможность получать всю информацию о обьекте (все пользовательские атрибуты и методы) через метод __str__.
#4. ** Создайте подклассы для класса животное - Собака, Птица, Змея. Реализуйте для обьектов размножение используя метод сложения обьектов.



# ЗАДАНИЕ 1
    # Напишите класс, отвечающий за животное. Реализуйте в классе атрибуты : количество лап, издаваемый звук, кличка.
    # Реализуйте в классе метод "издать звук". Количество лап и звук задается при инициализации и имеет ограничения (ограничения придумайте сами).
    # Кличка дается после инициализции. Создайте несколько обьектов класса, напр кошка, собака, птица, и тд.

# class Animal():
#     _legs = None
#     _sound = None
#     name = None
#
#     def play_sound(self):
#         return self._sound
#
#     def __str__(self):
#         return f"Name: {self.name}, Legs: {self.legs}, Sound: {self.sound}"
#
#     def __init__(self, legs, sound):
#         self.legs = legs
#         self.sound = sound
#         self.name = input("Write a name of this animal ---> ")
#
#
#     def get_legs(self):
#         return self._legs
#
#     def set_legs(self, legs):
#         if legs > 4 :
#             raise ValueError
#         self._legs = legs
#
#     def get_sound(self):
#         return self._sound
#
#     def set_sound(self, sound):
#         if sound.lower() not in ("roar", "shhh", "bark", "miau", "pipipi"):
#             return ValueError
#         self._sound = sound
#
#     legs = property(get_legs, set_legs)
#     sound = property(get_sound, set_sound)
#
#
# cat = Animal(legs = 4, sound = "miau")
# print(cat)
# dog = Animal(legs = 4, sound = "bark")
# print(dog)
# snake = Animal(legs = 0, sound = "shhh")
# print(snake)
# chicken = Animal(legs=2, sound = "pipipi")
# print(chicken)



# ----------------------


# ЗАДАНИЕ 2
    # Напишите декоратор, который бы сообщал время запуска и время завершения функции.
    # (узнать текущее время можно с помощью модуля time

# import time
#
# def decorator(foo):
#     start = time.time()
#     x = foo
#     stop = time.time()
#     print(f"Your time to write {x} is {stop-start} sec.")
#
# @decorator
# def question ():
#     return input ("Enter your Name and Surname ---> ")
#
# question()


# ----------------------

# ЗАДАНИЕ 4
#     Создайте подклассы для класса животное - Собака, Птица, Змея. Реализуйте для обьектов размножение используя метод сложения обьектов.

# from random import randint
#
# class Animal():
#     _legs = None
#     _sound = None
#     _name = None
#     _sex = None
#
#     def play_sound(self):
#         return self._sound
#
#     def get_legs(self, legs):
#         return self._legs
#
#     def set_legs(self, legs):
#         if legs > 4 :
#             raise ValueError
#         self._legs = legs
#
#     def get_sound(self):
#         return self._sound
#
#     def set_sound(self, sound):
#         if sound.lower() not in ("roar", "shhh", "bark", "miau", "pipipi"):
#             return ValueError
#         self._sound = sound
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if not isinstance(name, str):
#             return ValueError
#         self._name = name
#
#     def get_sex(self):
#         return self._sex
#
#     def set_sex(self, sex):
#         if sex.lower() not in ("male", "female"):
#             return ValueError
#         self._sex = sex
#
#     legs = property(get_legs, set_legs)
#     sound = property(get_sound, set_sound)
#     name = property(get_name, set_name)
#     sex = property(get_sex, set_sex)
#
#
# class Cat (Animal):
#     type = "cat"
#     name = None
#     _sex = None
#
#     def __init__(self, legs, sound, sex):
#         super().__init__()
#         self.legs = legs
#         self.sound = sound
#         self.sex = sex
#         self.name = input(f'Write a name of this {self.type} ---> ')
#
#     def __str__(self):
#         return f"Name: {self.name}, Legs: {self.legs}, Sound: {self.sound}, Sex: {self.sex}"
#
#     def __add__(self, other):
#         if self.sex == other.sex:
#             print(f"Извините, животные типа {self.type} останутся без потомства - они однополые.")
#             raise ValueError
#         elif self.type != other.type:
#             print(f"Вы вообще нормальный скрещивать {self.type} и {other.type}?")
#             raise ValueError
#
#         if randint(0, 1) == 0:
#             x = "Male"
#         else:
#             x = "Female"
#
#         return Cat(4, "miau", x)
#
# class Dog(Animal):
#     type = "dog"
#     name = None
#
#     def __init__(self, legs, sound, sex):
#         self.legs = legs
#         self.sound = sound
#         self.sex = sex
#         self.name = input(f'Write a name of this {self.type} ---> ')
#
#     def __srt__(self):
#         return f"Name: {self.name}, Legs: {self.get_legs}, Sound: {self.get_sound}, Sex: {self.sex}"
#
#     def __add__(self, other):
#         if self.sex == other.sex:
#             print(f"Извините, животные типа {self.type} останутся без потомства - они однополые.")
#             raise ValueError
#         elif self.type != other.type:
#             print(f"Вы вообще нормальный скрещивать {self.type} и {other.type}?")
#             raise ValueError
#
#         if randint(0, 1) == 0:
#             x = "Male"
#         else:
#             x = "Female"
#
#         return Dog(4, "bark", x)
#
# class Bird(Animal):
#     type = "bird"
#     name = None
#
#     def __init__(self, legs, sound, sex):
#         self.legs = legs
#         self.sound = sound
#         self.sex = sex
#         self.name = input(f'Write a name of this {self.type} ---> ')
#
#     def __srt__(self):
#         return f"Name: {self.name}, Legs: {self.get_legs}, Sound: {self.get_sound}, Sex: {self.sex}"
#
#     def __add__(self, other):
#         if self.sex == other.sex:
#             print(f"Извините, животные типа {self.type} останутся без потомства - они однополые.")
#             raise ValueError
#         elif self.type != other.type:
#             print(f"Вы вообще нормальный скрещивать {self.type} и {other.type}?")
#             raise ValueError
#
#         if randint(0, 1) == 0:
#             x = "Male"
#         else:
#             x = "Female"
#
#         return Bird(2, "pipipi", x)
#
# class Snake(Animal):
#     type = "snake"
#     name = None
#
#     def __init__(self, legs, sound, sex):
#         self.legs = legs
#         self.sound = sound
#         self.sex = sex
#         self.name = input(f'Write a name of this {self.type} ---> ')
#
#     def __srt__(self):
#         return f"Name: {self.name}, Legs: {self.get_legs}, Sound: {self.get_sound}, Sex: {self.sex}"
#
#     def __add__(self, other):
#         if self.sex == other.sex :
#             print(f"Извините, животные типа {self.type} останутся без потомства - они однополые.")
#             raise ValueError
#         elif self.type != other.type:
#             print(f"Вы вообще нормальный скрещивать {self.type} и {other.type}?")
#             raise ValueError
#
#         if randint(0,1) == 0:
#             x="Male"
#         else:
#             x="Female"
#
#         return Snake(0, "Shhh", x)
#
# print("Let's create some cat - boy:")
# cat_1 = Cat(legs = 4, sound = "miau", sex = "male")
# print("Let's create another cat - girl:")
# cat_2 = Cat(legs = 4, sound = "miau", sex = "female")
# print("They have produced a vaby:")
# cat_3 = cat_1 + cat_2
#
# print("Let's create some dog - boy:")
# dog_1 = Dog(legs = 4, sound = "bark", sex = "male")
# print("Let's create another dog - girl:")
# dog_2 = Dog(legs = 4, sound = "bark", sex = "female")
# print("They have produced a vaby:")
# dog_3 = dog_1 + dog_2
#
# bird_1 = Bird(legs = 2, sound = "pipipi", sex = "male")
# snake_1 = Snake(legs = 0, sound = "Shhh", sex = "female")
# creature = bird_1 + snake_1

