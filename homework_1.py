class ComplexNumbers:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
     
    def get_x(self):
        return self._x, self._y

    def __add__(self, other):
        return ComplexNumbers(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return ComplexNumbers(self._x - other._x, self._y - other._y)

    def __mul__(self, other):
        return ComplexNumbers(self._x * other._x, self._y * other._y)

    # def __div__(self, other):
    #     return ComplexNumbers(self._x / other._x, self._y / other._y)

    def __floordiv__(self, other):
        return ComplexNumbers(self._x // other._x, self._y // other._y)
         
    def __mod__(self, other):
        return ComplexNumbers(self._x % other._x, self._y % other._y)

    def __and__(self, other):
        return ComplexNumbers(self._x & other._y, self._y & other._y)

a = ComplexNumbers(12,18)
b = ComplexNumbers(4,1)
d = ComplexNumbers(6,5)
c = a * b

print(c.get_x())