# Конспект. Заняття 2. Робота з строками. Методи. Масиви. Умови. Цикли. Python 13-17
#РОБОТА З КОНСОЛЮ

#Методы

#Работа с регистрами строк
a = 'szdfhvxkjh'
#a. Вывод в консоль всех методов работы с данным типлом переменной

a.upper() #Все буквы заглавные
b = a.upper()
'szdfhvxkjh'.upper() #Без использования переменных

a.capitalize() #Первая буква заглавнае

#Функция len - длина строки
len ("wlkafjhedvg")
my_str = input("Напиши здесь что-либо")
len(my_str)



#метод replace (a, b)
my_str = "lakdajhwafgac"
my_new_str = my_str.replace("a", "A")
print (my_new_str)


#метод find
my_str = "lakdajhwafgac"
my_str.find("a") #Возвращает индекс первого вхождения
my_str.find("a", 3) #Возвращает вхожденияначинает поиск от 3го индекса


#Работа с методами int-а
b = 10
b. #Вывод в консоль всех методов работы с данным типлом переменной

#Где искать информацию о доступных методах - через .__doc__
a = "wafvsdbfd"
a.capitalize.__doc__



#ЭКРАНИРОВАНИЕ СИМВОЛОВ
print ("'wafelkj'vsdafkeljs")
print ('wafelkj\'vsdafkeljs') #Символ \ экранирует следующий за ним символ
print ("fajekhgv\nwkqldjfaesh") #Символ \n считается в python перносом строки
print ("fajekhgv\\nwkqldjfaesh") #Теперь отработает нормально





#INPUT

my_str = input("Напиши здесь что-либо")
print (my_str)








#Вставка значений в строку
a = 10
print (f"adfhj {a} awdfesgb")


#Индексы в строке и что с ними можно делать. СРЕЗЫ
my_str = "0123456789"
my_str [0] #Вывод элемента строки с индексом 0
my_str[0:3] #Вывод элементов строк с индексом от 0 до 3 (не включая 3)
my_str[ :3] #То же самое
my_str[2: ] #От второго индекса до конца
my_str [15] #Ошибка, такого индекса нет
my_str[-2] #Идёт в обратном направлении
my_str[-2:9]
my_str[0:7:2] #Третье число указывает шаг, то есть в данном случае будет выводиться каждый второй символ
my_str[ : : -1] #Вывод в обратном порядке всего массива
my_str[5 : 0 : -2] #Вывод в обратном порядке части массива с заданным шагом
my_str[len(my_str)//2] #Как найти серединный элемент массива (если строка нечётная)


#Метод .split() разделяет строку по заданному значению.
my_str = "0123456789"
my_str.split("5")
my_str = "example-xample-xample-xample"
my_str.split("-")
my_str = "dwafeknj faljksdbv wakdjfb awdkjfb kdwjb"
my_str.split(" ")
"afesvfd afsdv awfdsvx fdb".split(" ")

my_str = "dwafeknj faljksdbv wakdjfb awdkjfb kdwjb" #Как меняется тип данных
type (my_str) #Тип str
x = my_str.split(" ")
type (x) #Тип list







#Тип list - массив
my_list = [1, 5.9837 , 0, my_str, "fasdvf", True, False, None]
print (my_list)
print (my_list[3])

#Добавление данных в конец массива - метод .append
my_list.append("append")
print (my_list)
my_list.append(my_str)
print (my_list)

#Вставка значений в list . В отличии от строки, в list можно менять значение элементов, указав их индекс.
my_list [0] = "Zamena"
print (my_list)
#list также поддерживает СРЕЗЫ

#Работа с вложенными массивами и строками
my_list = ["Привет мир!", [1, 2, 3, 4, 5], 788.877, [5, 4, 3, 2, 1]]
my_list[0][4]
my_list[0][4].split(" ") #Работаем с текстом методами работы с текстом.
my_list[1][4] + my_list[3][0] #Складываем конкретные значения двух массивов
my_list[1][3] = "Тут замена" #Заменяем конкретное значение


#Сложение массивов
my_list1 = ["akjefh", 7685, [3,4,5,6,6], True]
my_list2 = [False, [a, b, "c", "d", "e, f"], 9876, "jhgaffndv" ]
my_list1 + my_list2


#Умножение массивов
my_list1 = ["akjefh", 7685, [3,4,5,6,6], True]
my_list * 2

#Делить и вычитать массивы нельзя. Так же, как и со строками.

#Оператор in
my_list1 = ["akjefh", 7685, [3,4,5,6,6], True]
7685 in my_list1
958 in my_list1

#Функция len
my_list1 = ["akjefh", 7685, [3,4,5,6,6], True]
len(my_list1)










#3 способа управления программой: действие, условие, цикл.

#Действия
x = 5
y = 6
z = x + y

#Условие
if 'условие, которое проверяется на True и False' :
    'реализация' #Принцип работы табуляцмей или 4мя пробелами.

if x < y :
    z = x + y
    print (z)

if True : #True
    print ("Hello")

if "kjhfa" : #Непустая строка при преобразовании в bool даёт True
    print ("Yes")


if z : #Проверка, существует ли непустая переменная с
    print ("Wow")



#Условие + else

if 'условие, которое проверяется на True и False' :
    'реализация'
else:
    'реализация2'

if 5 == 5 :
    print ("Yes")
else :
    print ("Oh my God!")



#Условие + elif + else
a = 5
if a > 5 :
    print ("Yes")
elif a == 5 :
    print ("Wow")
else :
    print ("Oh my God!")


#Инвертирование True и False - оператор not
not True
not False
not "a"
not ""

#Проверка на False - применение - оператора not
if a:
    print ("---------")

a = True
if not a :
    print ("-------")


#Логические операторы or и and
z = a or b
z = a and b

if x or (not y and True) : #Во втором примере вставить вместо or and
    print (1)
elif y :                    #В третьем примере добавить not
    print (True)
else :
    print ("Lalalal")







#ЦИКЛЫ

#Цикл while

while True :
    print ("Akukaracha")

a = 1  # type: int
while a != 10 :
    print (a)
    a = a + 1

b = 0
while True :
    print ("fejkshdvg")
    if b == 10 :
        break           #break - условие выхода из цикла внутри него.
    b = b + 1


while True :
    print ("dawf")
    if True :
        continue           #break - условие выхода из цикла внутри него.
    print ("fesgbfd")
    print ("fesgbfd")
    print ("fesgbfd")
    print ("fesgbfd")





#Упрощение работы с счётчиками
a += 1  #Заменяет выражение a = a + 1
a -= 1
a *= 2
a /= 2

x=10
y=0
while x > y :
    print (f"fasdgv {y}")
    y +=1



#Цикл for
for i in "kawejfhdvkjbsvdkjb" :
    print (i)

my_list = ["akjefh", 7685, [3,4,5,6,6], True]
for i in my_list :
    print (i)


my_list = ["akjefh", ["a","b","c","d","e","f"], [3,4,5,6,6], "faekhsvb"]
for i in my_list :
    print (i[1])


#Функция range - создаёт счётчик, содержит только int
for i in range(10) :
    print (i)

for i in range(5, 10) : #От значения 5 до 10
    print (i)

for i in range(5, 10, 2) : #От значения 5 до 10, с шагом 2
    print (i)

lst = []
for i in range(5):
    lst.append(i**i)
    print (lst)




#Tuple - кортеж, неизменяемый список
t = (1,2,3)
t = tuple()
type(t)

t[2] #Обращение по индексу сработает
t[2] = 5 #Поаытка перезаписать что-то в кортеже выдаст Ошибку






#Преобразование str, list и tuple
str(12345)
a = list (str(12345))
b = str (a)
c = list (b)

tuple("12324354657689")
str(tuple("12324354657689"))
int(tuple("12324354657689")) #Ошибка

a = (2,4,"dafsd", [11,22,"dsa"])
b = list(a)