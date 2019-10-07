# Create a data structure class Stack, Queue. 
# Create a complex number class and implement arithmetic operations for it.

class DataSteck:
    pass


class DataQueue:
    pass





class ComplexNumbers:
    
    def __init__(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary
     
    def get_x(self):
        return self._real, self._imaginary

    def __add__(self, other):
        return ComplexNumbers(self._real + other._real, self._imaginary + other._imaginary)

    def __sub__(self, other):
        return ComplexNumbers(self._real - other._real, self._imaginary - other._imaginary)

    def __mul__(self, other):
        return ComplexNumbers(self._real * other._real, self._imaginary * other._imaginary)

    # def __div__(self, other):
    #     return ComplexNumbers(self._real / other._real, self._imaginary / other._imaginary)

    def __floordiv__(self, other):
        return ComplexNumbers(self._real // other._real, self._imaginary // other._imaginary)
         
    def __mod__(self, other):
        return ComplexNumbers(self._real % other._real, self._imaginary % other._imaginary)

    def __and__(self, other):
        return ComplexNumbers(self._real & other._real, self._imaginary & other._imaginary)


a = ComplexNumbers(2,18)
b = ComplexNumbers(4,1)
d = ComplexNumbers(6,5)
c = a & b

print(c.get_x())