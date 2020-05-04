Конспект. Заняття 5. ФУНКЦИИ. Python 13-17

def foo():
    print('in function')
    print('res--> ', 1 + 2)

print('before')
foo()
print('after')

-----------------

Область видимости

x = 10

def foo2():
    x = 20
    print('in function')
    print('x-->', x)

foo2()

print(x)

---------------
x = 15

def foo3():
    global x     #Использование глобальной переменной
    print(x)
    x = 25

print(x)
foo3()
print(x)
-----------------

y = 30

def foo4():
    x = 10
    return x * y

z = foo4()
print(type(z))

-------------------

y = foo4()

print(y)
x = 1
y = 2
z = 3

def foo5(a, b, c):
    print('a-->',a)
    print('b-->',b)
    print('c-->',c)

foo5(x, z, 'wdedfg', d=1)

foo5(z, x, None)

foo5(z, y, [])

foo5(1, {'a': 'b'}, 12345)

----------------


def foo6(a, b=10):
    print('a-->', a)
    print('b-->', b)

foo6('qwert')
foo6('qwert', 'B is here')

-------------------

def bar(a, b):
    print('a-->', a)
    print('b-->', b)

bar(1, 2)
# bar(a=1, b=2)
bar(b=1, a=2)

# ------------------

# def bar1(a, b=1, c=2):
#     print('a-->', a)
#     print('b-->', b)
#     print('c-->', c)
#
# def bar1(a, b=1):
#     print('a-->', a)
#     print('b-->', b)
#
# bar1(1, c=[], b={})

# bar1 = 1234567

# --------------------


# def bar2(my_str, val):
#     for i in my_str:
#         if i == val:
#             return [i, 1]     #RETURN - возвращает вычисление внутри функции. Может возвращать пачку значений
#         elif i == 'a':
#             print('a found!')
#
# data = 'iuaytrewasdfghjkuytrexcvb'
# value = 'r'
#
# x = bar2(data, value)                 #RETURN вернёт 1 значение - массив/кортеж
# print(x)


# def bar2(my_str, val):
#     for i in my_str:
#         if i == val:
#             return i, 1               # тут нет скобок
#         elif i == 'a':
#             print('a found!')
#
# data = 'iuaytrewasdfghjkuytrexcvb'
# value = 'r'
#
# x, y = bar2(data, value)              #RETURN вернёт 2 значения x и у
# print(x)


# ----------------------

# a = 10
# b = 20
# c = 30
#
# def bar5(*args):              # Использование * даёт возможность передавать в функцию неопределённое количество аргументов. Воспринимается как кортеж из тех аргументов, которые к нему пришли.
#     # print(type(args))
#     print(args[0])
#
# bar5()
# bar5(1,2,3,3,5,6,7,8,9,0,4)
# bar5(a)
# bar5(c,b,c)
#
#
# ---------------------
#
# def bar(a, b, c):
#     print('a-->', a)
#     print('b-->', b)
#
# x = 123
#
# # bar(a=x, b=x, c = 1)
# bar(x, 1, x**x)

# --------------------

# a = 10
# b = 20
# c = 30
#
# def bar5(a, *args):
#     # print(type(args))
#     print(args)
#
# bar5(1, 2, 3, 4)
#
# def bar6(a, b=3, *args):
#     print(args)
#
# bar6(1, 2, 3, 4)
#
# -----------------------

# def bar7(a=2, **kwargs):          # **KWARGS - принимает имена и значения переменных
#     print('a-->', a)
#     print(kwargs)
#
# bar7(1, b=2, c=3)

# -------------------------
#def bar7(**kwargs):          # **KWARGS - принимает имена и значения переменных
#     print('a-->', a)
#     print(kwargs)

# d = {'a': 1, 'b': 2, 'z': 4}      #Аргумент передаём в виде словаря
#
# bar7(**d)                         # **d - Распаковка словаря по аргументам, функция её расшифрует как bar7(a=1, b=2, z=4)
#
# ---------------------------
#
# def bar8(a, **kwargs):
#     print('a-->', a)
#     print(kwargs)
#
# bar8(**d)
#
# def bar9(a, b=5, *args, **kwargs):
#     print('a-->', a)
#     print(kwargs)
#

# -----------------------
# def bar10(*args, **kwargs):       # ПРИМЕР передачи в функцию и *args и *kwargs
#     print('args-->', args)
#     print('kwargs-->', kwargs)
#
# d = {'a': 1, 'b': 2, 'z': 4, 'ddd': 'qwerghj'}
# L = [1,2,3,4,5]
#
# bar10(*L, **d)
# bar10(L, d)           #Все попадут в args

# bar10('qqq', 13, vfr=750, **d)

