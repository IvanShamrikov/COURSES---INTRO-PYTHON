# Занятие 11. ИТЕРАТОРЫ. ГЕНЕРАТОРЫ PROPERTY 13-17

# Итератор можно получить из итерируемых объектов. То есть из тех, которые поддаются перебору:


my_list = [1, 2, 3, 4, 5, 6]
# my_list = "<Jhkjkjawjbjkbaefkj"
my_iterator = iter(my_list)
# my_iterator = iter(12345)       #Сломается, int не является интерируемым

print(my_iterator)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# print(next(my_iterator))      #Ошибка, у итератора нет 7-го значения

for i in "awjkfehb":       # tmp = iter("awjkfehb")
    # next(tmp)
    print(i)

my_iterator = my_list.__iter__()        #равносильные записи
my_iterator = iter(my_list)


# Создание собственного итератора.
# Нужно, чтоб выдавать определенные ачивки в разное время выполнения программы.
# Например, у нас есть 100 яблок, которые выдаются игроку при прохождении чекпоинта:
# В каждом чекпоинте вызываем итератор и он выдаёт ачивку и уменьшает оставшееся к выдаче количество

def my_iter(limit):
    while limit > 0:
        yield limit     #yield - превращает в итератор. отдаёт значение и замирает до следующего вызова функции
        limit -= 1

m_i = my_iter (5)

print(next(m_i))
print(next(m_i))
print(next(m_i))
print(next(m_i))
print(next(m_i))



# ------------

def my_iter(limit):
    while limit > 0:
        if limit%2 == 0:
            yield limit     #будет выдавать только на чётных значениях итератора
        limit -= 1

m_i = my_iter (5)

for i in m_i:
    print("my iter", i)


# ----------------------

# Создание итерируемых объектов

class A():
    __limit = 0

    def __init__(self, limit):
        self.__limit = limit

    def __iter__(self):             # Метод, который превращает объект в итератор
        return self

    def __next__(self):
        if self.__limit > 0:
            self.__limit -=1
            return self.__limit+1
        else:
            print("Empty Iterator")
            raise StopIteration

m_i_cls = A(5)

for i in m_i_cls:
    print(i)





for i in m_i_cls:       #Второй раз не запустится, потому что итератор уже пустой.
    print(i)

# Для того, чтоб этот объект можно было итерировать снова и снова, нужно переопределить стартовое значение:

class A():
    __limit = 0
    __counter = 0                              #Добавили тут

    def __init__(self, limit):
        self.__limit = limit

    def __iter__(self):
        self.__counter = self.__limit         #Добавили тут. На каждом новом вызове счётчик будет перезаписываться.
        return self

    def __next__(self):
        if self.__counter > 0:              #Работаем с счётчиком
            self.__counter -= 1
            return self.__counter + 1
        else:
            print("Empty Iterator")
            raise StopIteration


m_i_cls = A(5)

for i in m_i_cls:
    print(i)

for i in m_i_cls:           #Теперь итератор будет запускаться столько, сколько нужно, потому что мы зафиксировали его лимит и работаем с счётчиком
    print(i)



# -----------------------------


# ГЕНЕРАТОРЫ - итераторы, которые сохраняют какие-то значения

x = [i for i in m_i_cls]
print(x)
x = {i: i**2 for i in m_i_cls}
print(x)
x = (i for i in m_i_cls)

print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


class Triangle():

    def __init__(self, a,b,c):
        self._x = a
        self._y = b
        self._z = c

    def __iter__(self):
        self._points = (self._x, self._y, self._z)
        self._point_iter_index = 0
        return self

    def __next__(self):
        if self._point_iter_index < len(self._points):
            self._point_iter_index += 1
            return self._points[self._point_iter_index - 1]
        else: raise StopIteration

t = Triangle("point a", "point b", "point c")

for i in t:
    print(i)