# Описать с помощью классов кухню в виде диаграммы
# (приммер https://www.intuit.ru/EDI/23_04_17_1/1492899714-28128/tutorial/356/objects/2/files/02_05.gif).
# Реализовать наследованием классов мебель, технику, посуду с описанием свойств и методов.
# Описать все то же с помощью питона.
#
#
#
# почитать:
#
# https://pythonworld.ru/osnovy/obektno-orientirovannoe-programmirovanie-obshhee-predstavlenie.html
#
# https://metanit.com/python/tutorial/7.1.php
#


# Задача **
# Капиталл-Шоу "Поле Чудес"
# Компьютер загадывает слово.
# Пользователь пытается его угадать за n попыток
# Если угадывает - слово появляется в виде s _ o w m _ n
#
#
class Game:
    def __init__(self, word):
        self.guessed_letters = []
        self.word = word

    def play(self):
        for index in range(6):
            dashed_word = ""

            print("Guess a letter")
            guess = input()
            self.guessed_letters.append(guess)

            for char in self.word:
                if char in self.guessed_letters:
                    dashed_word += char
                else:
                    dashed_word += "_  "

            print(dashed_word)
            print(self.guessed_letters)


game = Game("snowman")
game.play()


