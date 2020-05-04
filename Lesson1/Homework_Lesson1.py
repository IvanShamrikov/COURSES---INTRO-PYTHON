#1. Дано два числа (a=10, b=30). Вывести на экран результат математического взаимодействия (+, -, *, / ) этих чисел.
print('Task 1')
print('----------------')
a = 10
b = 30
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("\n")

#2. Создать переменную и записать ??? в нее результат логического взаимодействия (<, > , ==, !=) этих чисел После этого ывести на экран значение полученой переменной.
print('Task 2')
print('----------------')
c = a < b
print("a < b =", c)
c = a > b
print("a > b =", c)
c = a == b
print("a == b =", c)
c = a != b
print("a != b =", c)
print("\n")

#3. Создать переменную - результат конкатенации (сложения) строк str1="Hello " и str2="world". Вывести на ее экран.
print('Task 3')
print('----------------')
str1 = "Hello "
str2 = "world"
str_res = str1 + str2
print(str_res, '\n')


#4. Используя переменные a и b сформировать строку "First variable is [тут знаение переменной a], second variable is [тут знаение переменной b]. Their sum is [тут их сумма]."
print('Task 4')
print('----------------')
string = "First variable is " + str(a) + ", second variable is " + str(b) + ". Their sum is " +  str(a + b) + "."
print(string)

