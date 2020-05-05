# Занятие 10. ПРАКТИКА 13-17

# 1
# Написать класс Point, отвечающий за точку на координатной плоскости.
# Обьект класса Point должен обязательно иметь координаты и название.

# 2
# # Написать класс, Line отвечающий за отрезок.
# # Обьект класса Line инстанциируется с помощью двух обьектов класса Point

# 3
# # Написать класс, Triangle отвечающий за треугольник.
# #     Более простое задание - Обьект класса Triangle инстанциируется с помощью трёх обьектов класса Point. Важно проверить, чтоб ни одна точка не совпала с другой.
# #     Задача с двумя ** - Обьект класса Triangle инстанциируется с помощью трёх обьектов класса Line. Важно проверить, чтоб было три пары одинаковых точек, иначе треугольник не сойдётся

class Point():
    _x = None
    _y = None
    _name = None

    def __init__(self, x, y, name):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self._x = x
            self._y = y
        self.name = name

    def __str__(self):
        return f"Point {self.name.upper()} ({self.x}, {self.y})"

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    name = property(get_name, set_name)



2
# Написать класс, Line отвечающий за отрезок.
# Обьект класса Line инстанциируется с помощью двух обьектов класса Point

class Line():
    _point_A = None
    _point_B = None

    def __init__(self, obj_pointA, obj_pointB):
        if isinstance(obj_pointA, Point) and isinstance(obj_pointB, Point):
            if obj_pointA.x == obj_pointB.x and obj_pointA.y == obj_pointB.y:
                raise ValueError
            else:
                self.point_A = obj_pointA
                self.point_B = obj_pointB

    def __str__(self):
        return f'Line from {self.point_A.x}:{self.point_A.y} to {self.point_B.x}:{self.point_B.y}'

    def get_point_A(self):
        return self._pointA

    def set_point_A(self,obj_pointA):
        self._pointA = obj_pointA

    def get_point_B(self):
        return self._pointB

    def set_point_B(self,obj_pointB):
        self._pointB = obj_pointB

    obj_pointA = property(get_point_A, set_point_A)
    obj_pointB = property(get_point_B, set_point_B)







class Triangle():
    _line_1 = None
    _line_2 = None
    _line_3 = None
    __point_X = None
    __point_Y = None
    __point_Z = None

    def __init__(self, line_1, line_2, line_3):
        self.line_1 = line_1
        self.line_2 = line_2
        self.line_3 = line_3
        if self.check_lines(): print("IT'S TRIANGLE")
        else: print("IT'S NOT TRIANGLE")

    def __str__(self):
        if self.check_lines():
            return f'Triangle with points {self.__point_X.x}:{self.__point_X.y}, {self.__point_Y.x}:{self.__point_Y.y}, {self.__point_Z.x}:{self.__point_Z.y},'
        else:
            return "There is no points"

    def get_line_1(self):
        return self._line_1

    def set_line_1(self, line_1):
        if isinstance(line_1, Line):
            self._line_1 = line_1

    def get_line_2(self):
        return self._line_2

    def set_line_2(self, line_2):
        if isinstance(line_2, Line):
            self._line_2 = line_2

    def get_line_3(self):
        return self._line_3

    def set_line_3(self, line_3):
        if isinstance(line_3, Line):
            self._line_3 = line_3

    line_1 = property (get_line_1, set_line_1)
    line_2 = property(get_line_2, set_line_2)
    line_3 = property(get_line_3, set_line_3)

    # ПРОВЕРКА ВОЗМОЖНОСТИ СОЗДАНИЯ ТРЕУГОЛЬНИКА ИЗ ЭТИХ ЛИНИЙ
    def check_lines(self):
        lst = [self.line_1, self.line_2, self.line_3]

        all_points = []
        for i in lst:
            all_points.append(i.point_A)
            all_points.append(i.point_B)

        tpl = {}
        for i in  all_points :
            if i in tpl.keys():
                tpl[i] +=1
            else:
                tpl.setdefault(i, 1)

        for i in tpl:
            if tpl[i] != 2:
                return False


        # ТАКЖЕ ПОСЛЕ ВЫЯВЛЕНИЯ ВЕРШИН ТРЕУГОЛЬНИКА НУЖНО ЗАПИСАТЬ ТОЧКИ ВЕРШИН КАК ОБЪЕКТЫ В АРГУМЕНТ ОБЪЕКТА ТРЕУГОЛЬИК
        args_points = [key for key in tpl.keys()]
        self.__point_X = args_points[0]
        self.__point_Y = args_points[1]
        self.__point_Z = args_points[2]


        return True         #Прошёл все проверки


pointA = Point(name = "a", x = 3, y = 2)
pointB = Point(name = "b", x = 2, y = 6)
pointC = Point(name = "c", x = 3, y = 6)
pointD = Point(name = "d", x = 5, y = 6)
pointE = Point(name = "e", x = 4, y = 9)
pointF = Point(name = "f", x = 2, y = 7)
pointG = Point(name = "g", x = 1, y = 5)

line_1 = Line(pointA, pointB)
line_2 = Line(pointA, pointC)
line_3 = Line(pointB, pointC)

line_4 = Line(pointD, pointA)
line_5 = Line(pointD, pointC)
line_6 = Line(pointG, pointA)

triangle1 = Triangle(line_1, line_2, line_3)
triangle1.check_lines()
print(triangle1)

triangle2 = Triangle(line_4, line_5, line_6)
triangle2.check_lines()
print(triangle2)


