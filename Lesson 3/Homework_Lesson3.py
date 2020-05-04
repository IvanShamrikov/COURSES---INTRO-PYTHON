# ЗАДАЧА 1
# Пользователь вводит строку произвольной длины. Найти в строке самое длинное слово, в котором присутствуют подряд две согласные буквы.
# Если в строке присутс

# ЗАДАЧА 2
# Есть числовой ряд от 1 до N. Нужно найти все числа, которые без остатка делятся на M (M<=N).
# Например, нужно найти в числовом ряду от 1 до 1000, которые без остатка делятся на 13







# ЗАДАЧА 1
# Пользователь вводит строку произвольной длины. Найти в строке самое длинное слово, в котором присутствуют подряд две согласные буквы.
# Если в строке присутствует слово с тремя согласными буквами подряд - вывести сообщение "JOKER".

# --------------------------------------------------
# Version 1


my_str = (input("Type any string - ").lower()).split(" ")
glasnye = ["e","y","u","i","o","a", "0", "1","2","3","4","5","6","7","8","9"]

list = []
longest_word = ""

for word in my_str :
    tmp_word = word
    for letter in glasnye :
        if letter in word :
            tmp_word = tmp_word.replace(letter, ".")

    tmp_word1 = tmp_word.split(".")

    for char in tmp_word1 :
        if len(char) > 1 :
            if len(char) > len(longest_word) :
                longest_word = word
        if len(char) == 3 :
            print("JOKER")
            exit()

print(longest_word)


# --------------------------------------------------
# Version 2

my_str = (input("Type any string - ").lower()).split(" ")
soglasnye = "qwrtpsdfghjklzxcvbnm"

var = 0
longest_word = ""

for word in my_str :
    for letter in word :
        if letter in soglasnye :
            var += 1
            if var == 3 :
                print("JOKER")
                exit()
            elif var > 1 :
                if len(word) > len(longest_word):
                    longest_word = word
        else:
            var = 0

print(longest_word)


# --------------------------------------------------
# Version 3

user_data = input('your text')

words_list = user_data.split()
match_words = []

chr_list = 'wrtpsdfghklzxcbmn'

for word in words_list:
    tmp_char = ' '
    for char in word:
        if tmp_char in chr_list and char in chr_list:
            match_words.append(word)
            break
        tmp_char = char

tmp_word = ''
for word in match_words:
    if len(word) > len(tmp_word):
        tmp_word = word

print(tmp_word)




# ЗАДАЧА 2
# Есть числовой ряд от 1 до N. Нужно найти все числа, которые без остатка делятся на M (M<=N).
# Например, нужно найти в числовом ряду от 1 до 1000, которые без остатка делятся на 13

N = input('Введи число N - ')
M = input("Введи число M - ")
x = N // M
list = []

# ПЕРВЫЙ ВАРИАНТ

for y in range(1, x+1) :
    list.append(y*13)
print (list)

# ВТОРОЙ ВАРИАНТ

list = []
y = 0
while True:
    y += 13
    if y < N:
        list.append(y)
    else:
        break
print (list)


# ТРЕТИЙ ВАРИАНТ

list = []
x = N
while True:
    while x % M != 0:
        x -= 1
    while x != 0 :
        list.append(x)
        x -= 13
    break
print(list)


# ЧЕТВЕРТЫЙ ВАРИАНТ

for i in range (1, N+1) :
    if i % M == 0 :
        list.append(i)
print (list)