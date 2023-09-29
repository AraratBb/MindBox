from math import pi, sqrt

class Figure:
    """Конструктор должен принимать кортежи с координатами фигуры (Xi , Yi) метод area() находит площади с помощью формулы площади Гаусса"""
    def __init__(self, *args):
        for i in args:
            for j in i:
                if type(j) not in (float, int):
                    raise TypeError("Координаты должны быть числом")
        self.coords = args
        self.size = len(args)
        self.__X = []
        self.__Y = []
        for i in args:
            self.__X.append(i[0])
            self.__Y.append(i[1])

    def area(self) -> float:
        s = 0

        for i in range(self.size - 1):
             s += self.__X[i] * self.__Y[i + 1]

        s += self.__X[self.size - 1] * self.__Y[0]

        for i in range(self.size - 1):
             s -= self.__X[i + 1] * self.__Y[i]

        s -= self.__X[0] * self.__Y[self.size - 1]

        return abs(s) / 2

class Triangle(Figure):

    def __init__(self, a, b, c):

        if not all(type(i) == float for i in (a,b,c)) and not all(type(i) == int for i in (a,b,c)):
            TypeError("Координаты должны быть числом")

        r = sorted([a, b, c])
        if r[2] >= r[0] + r[1]:
            raise ValueError("Сумма длин любых двух сторон треугольника должна быть больше длины третьей стороны")

        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = sum((self.a,self.b,self.c))/2
        return sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))

    def isRight(self) -> bool:
        r = sorted([self.a, self.b, self.c])
        return 2 * self.area() == r[0] * r[1]

class Circle(Figure):
    """  """
    def __init__(self, rad: float|int):
        if type(rad) not in (float, int):
            raise TypeError("Радиус должен быть числом")
        if rad < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.rad = rad

    def area(self) -> float:
        return pi*(self.rad**2)
f = Figure(("1",1), (1,2))