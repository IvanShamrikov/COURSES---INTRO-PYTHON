# 1. В отдельном файле (пусть будет lib.py) разместить функцию, которая спрашивает пользователя Y\N (можно использовать из предидущего задания).
#     В основном файле (пусть будет main.py) попросить пользователя ввести с клавиатуры строку и вывести ее на экран.
#     Спросить у пользователя, хочет ли он повторить операцию (Y/N) используя импортированую из lib.py функцию.
#
# 2. Пишем игру ) Программа приветствует пользователя и просит задать диапазон чисел.
#     После ввода программа выбирает из введенного диапазона число и предлагает пользователю его угадать.
#     Если пользователь не угадал - предлагает пользователю угадать еще раз, пока он не угадает.
#     Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить.

        # 2.1 Вариация "Царство Драконов"
        # Вы находитесь в землях, заселёнными Драконами.
        # Перед собой Вы видите 2 пещеры.
        # В одной из них - дружелюбный дракон,
        # который готов поделиться с Вами сокровищем.
        # Во второй - жадный и голодный дракон, который мигом Вас съест.
        # В какую пещеру Вы войдёте (введите 1 или 2).
        # 1
        # Вы приближаетесь к пещере...
        # Её темнота заставляет Вас дрожать от страха...
        # Большой Дракон выпрыгивает перед Вами! Он раскрывает свою пасть и...
        # ... моментально Вас съедает
        # ... делится с Вами сокровищами.
        # Хотите сыграть еще раз? (да или нет)
        # да
#
# 3. Добавить в задание 2 счетчик попыток. Кроме диапазона чисел пользователь вводит количество попыток, за которые он может угадать число.
#     На каждом шаге сообщайте пользователю сколько попыток у него осталось.
#     Если пользователь не смог угадать за отведенное количество попыток сообщить ему об окончании (Looser!).
#     Спросить у пользователя, хочет ли он повторить игру (Y/N). Если Y - повторить.
#     Очень сильно к карме добавляет проверка введенных значений, причем не только на тип, но и на значение (включайте логику).


# ЗАДАНИЕ 4. ИГРА "ВИСЕЛИЦА"
# САМОЕ СЛОЖНОЕ.



# -------------------------------------

# ЗАДАНИЕ 1
# В отдельном файле (пусть будет lib.py) разместить функцию, которая спрашивает пользователя Y\N (можно использовать из предидущего задания).
# В основном файле (пусть будет main.py) попросить пользователя ввести с клавиатуры строку и вывести ее на экран.
# Спросить у пользователя, хочет ли он повторить операцию (Y/N) используя импортированую из lib.py функцию.


# import lib
#
# print("Hello World")
# while True:
#     answer = lib.question()
#     if answer.upper() == "Y" :
#         print("Hello World")
#     elif answer.upper() == "N":
#         break
#     else:
#         print("Ваш ответ " + answer + " не понятен. Попробуем еще раз")
#
# print("Всего доброго!")


# -------------------------------------
# ЗАДАНИЕ 2
# 2. Пишем игру ) Программа приветствует пользователя и просит задать диапазон чисел.
#     После ввода программа выбирает из введенного диапазона число и предлагает пользователю его угадать.
#     Если пользователь не угадал - предлагает пользователю угадать еще раз, пока он не угадает.
#     Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить.


# 2.1 Вариация "Царство Драконов"

# import random
# import time
#
# def displayIntro():
#     print(
#         '''Вы находитесь в землях, заселёнными Драконами.
# Перед собой Вы видите 2 пещеры.
# В одной из них - дружелюбный дракон,
# который готов поделиться с Вами сокровищем.
# Во второй - жадный и голодный дракон, который мигом Вас съест.''')
#     print()
#
# def chooseCave():
#     cave = ""
#     while cave != "1" or cave !="2":
#         print("В какую пещеру Вы войдёте (введите 1 или 2) ---> ")
#         cave = input()
#
#     return cave
#
# def checkCave(caveNumber):
#     print("Вы приближаетесь к пещере...")
#     time.sleep(2)
#     print("Её темнота заставляет Вас дрожать от страха...")
#     time.sleep(2)
#     print("Большой Дракон выпрыгивает перед Вами! Он раскрывает свою пасть и...")
#     time.sleep(2)
#
#     friendlyCave = str(random.randint(1,2))
#
#     if caveNumber == friendlyCave:
#         print("... делится с Вами сокровищами.")
#     else:
#         print("... моментально Вас съедает")
#
#
# playAgain = "да"
# while playAgain == "да":
#     displayIntro()
#     caveNumber = chooseCave()
#     checkCave(caveNumber)
#
#     print("Хотите сыграть еще раз? (да или нет) --->")
#     playAgain = input()









# ЗАДАНИЕ 3
# *Добавить в задание 2 счетчик попыток. Кроме диапазона чисел пользователь вводит количество попыток, за которые он может угадать число.
# На каждом шаге сообщайте пользователю сколько попыток у него осталось.
# Если пользователь не смог угадать за отведенное количество попыток сообщить ему об окончании (Looser!).
# Спросить у пользователя, хочет ли он повторить игру (Y/N). Если Y - повторить.
# Очень сильно к карме добавляет проверка введенных значений, причем не только на тип, но и на значение (включайте логику).
#


# def game ():
#     question = lib.get_question2()
#     goal = lib.get_goal(question)
#     tries_def = lib.get_tries ()
#     tries = tries_def
#
#     while tries !=0:
#         guess = lib.get_guess (question, tries)
#
#         tries -= 1
#
#         if lib.get_compare(guess, goal, tries_def, tries) == True or False:
#             break
#
#
#
# import lib
# game ()
# while True:
#     if lib.get_anotherGame():
#         game()
#     else:
#         print("Всего доброго!")
#         break








# ЗАДАНИЕ 4. ИГРА "ВИСЕЛИЦА"
# САМОЕ СЛОЖНОЕ.



# ----------------------
#
# *** WELCOME TO "HANGMAN" GAME ***
#   Let's start programming
#
# ----------------------



def displayBoard(missedLetters, correctLetters, secretWord, alfabet_board, theme):
    print(hangnam_pics[len(missedLetters)])
    print("Тема:",  theme)

    # Показываем состояние угадываемого слова на сейчас
    for index in range(len(secretWord)):
        dashed_word = ""
        for char in secretWord:
            if char in correctLetters:
                dashed_word = dashed_word + char + " "
            else:
                dashed_word += "_ "
    print("Слово на доске: ", dashed_word)


    # Показываем остальные буквы, доступные к угадыванию
    for index in range (len(alfabet)):
        if alfabet[index] in correctLetters or alfabet[index] in missedLetters:
            alfabet_board += "_ "
        else:
            alfabet_board = alfabet_board + alfabet[index] + " "
    print("Оставшиеся буквы: ", alfabet_board)


    #Показываем список ошибочных букв
    print("Ошибочные буквы: ", end = "")
    if missedLetters == "":
        print(" -", end="")
    else:
        for letter in missedLetters:
            print(letter + " ", end="")
    print()




def getRandomWord(themes):
    theme = random.choice(tuple(themes.keys()))
    word = random.choice(themes[theme])
    word = word.upper()
    return theme, word


def getGuess(correctLetters, missedLetters):
    while True:
        print()
        guess = input("Введите букву --> ").upper()
        if len(guess) != 1:
            print("Пожалуйста, введите одну букву.")
        elif guess in correctLetters or guess in missedLetters:
            print("Вы уже называли эту букву")
        elif guess in (" _") or guess not in alfabet or type(guess) != str:
            print("Это не буква. Введите БУКВУ")
        else:
            break
    print()
    return guess


def gameFinish(correctLetters, missedLetters, secretWord):
    unikLettersInSecretWord = set()
    for i in secretWord:
        unikLettersInSecretWord.add(i)

    if len(correctLetters) == len(unikLettersInSecretWord):
        print()
        print()
        print(f'''                  ПОЗДРАВЛЯЕМ! 
    Вы угадали слово {secretWord} и выиграли игру "ВИСЕЛИЦА"!''')
        return True
    elif len(missedLetters) == 6:
        print()
        print()
        print(f'''                  ИГРА ОКОНЧЕНА! 
    Вы не угадали слово {secretWord} и програли в игру "ВИСЕЛИЦА"!''')
        return True
    else:
        return False

def oneMore():
    while True:
        print()
        answer = input("Хотите сыграть еще раз? Введите да/нет --->").lower()
        if answer == "да":
            print()
            print()
            print()
            print()
            return True
        elif answer == "нет":
            return False
        else:
            print("Ваш ответ не понятен. Попробуем еще раз.")






def mainGame(themes):
    missedLetters = ""
    correctLetters = ""
    alfabet_board = ""

    print()
    print(
        '''                         Добро пожаловать в игру ВИСЕЛИЦА!
        У Вас есть 6 попыток угадать слово по заданной теме.
        После каждой неверной попытки к рисунку будет добавляться часть человечка.
        Если слово будет угадано до того, как человечек станет виден полностью - Вы выиграли!
                                    Удачи!
        ''')
    print()
    input("Нажмите ENTER для старта.")
    #Выбираем секретное слово
    theme, secretWord = getRandomWord(themes)


    while True:
        #Показываем текущее состояние игры
        displayBoard(missedLetters , correctLetters, secretWord, alfabet_board, theme)

        #Проверка результатов Игры - пишется последним
        if gameFinish(correctLetters, missedLetters, secretWord):
            if oneMore():
                mainGame(themes)
            else:
                break

        #Запрос пользователю на введение буквы. Проверка буквы.
        guess = getGuess(correctLetters, missedLetters)

        #Сверка буквы и запись в соответствующий массив
        if guess in secretWord:
            print("Такая буква есть в слове!")
            correctLetters += guess
            time.sleep(2)
        else:
            print("Такой буквы нет в слове!")
            missedLetters += guess
            time.sleep(2)






# ----------------------
#
# *** THE GAME CODE ***
#        below
#
# ----------------------





import random
import time

hangnam_pics = [
    '''
    +---+
        |
        |
        |
       ===''',
    '''
   +---+
   O    |
        |
        |
       ===''',
    '''
   +---+
   O    |
   |    |
        |
       ===''',
    '''
   +---+
   O    |
   |\   |
        |
       ===''',
    '''
   +---+
   O    |
  /|\   |
        |
       ===''',
    '''   
   +---+
   O    |
  /|\   |
  /     |
       ===''',
    '''  
   +---+
   O    |
  /|\   |
  / \   |
       ==='''
   ]
alfabet = ["А","Б","В","Г","Д","Е","Ë","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф", "Х","Ч","Ц","Ч","Ш","Щ","Ь","Ъ","Ы","Э","Ю","Я"]
goroda = ["Киев", "Одесса", "Харьков", "Львов", "Николаев", "Житомир", "Полтава", "Чернигов"]
zhyvotnye = ["аист","акула","бабуин","баран", "тритон", "черепаха", "ястреб", "ящерица", "муравей","барсук","медведь", "медоед", "муравьед", "панда", "ленивец"]
themes = {"Города Украины": goroda, "Животные": zhyvotnye}

mainGame(themes)
print()
print("                 ВСЕГО ДОБРОГО!")
