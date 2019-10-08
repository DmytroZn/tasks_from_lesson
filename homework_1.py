# Create a data structure class Stack, Queue. 
# Create a complex number class and implement arithmetic operations for it.

class DataStack:

    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items
    
    def push(self, value):
        self._value = value
        self._items.append(self._value)
    
    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            return None
    
    def back(self):
        return self._items[-1]
    
    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def clear(self):
        self._items = []

a = DataStack()
a.push(4)
a.push(5)
a.push(6)
print(a.get_items())
a.pop()
print(a.get_items())
print(a.back())
print(a.get_items())
print(a.is_empty())
print()
a.clear()
print(a.get_items())
a.push(5)
a.push(6)
print(a.get_items())
l = a.pop()
print(a.get_items())
print(l)
a.push(3)
print(a.size())

h = a.back()
print(h)
print(a.get_items())
a.pop()
a.pop()
a.pop()
a.pop()
a.clear()


class DataQueue(DataStack):
    
    def pop(self):
        try:
            return self._items.pop(0)
        except IndexError:
            return None

    def front(self):
        return self._items[0]


b = DataQueue()
b.push(5)
b.push(4)
b.push(6)
print()
print(b.get_items())
b.pop()
print(b.get_items())
print(b.front())


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

    def __truediv__(self, other):
        return ComplexNumbers(self._real / other._real, self._imaginary / other._imaginary)

    def __floordiv__(self, other):
        return ComplexNumbers(self._real // other._real, self._imaginary // other._imaginary)
         
    def __mod__(self, other):
        return ComplexNumbers(self._real % other._real, self._imaginary % other._imaginary)

    def __and__(self, other):
        return ComplexNumbers(self._real & other._real, self._imaginary & other._imaginary)


a = ComplexNumbers(2,18)
b = ComplexNumbers(4,1)
d = ComplexNumbers(6,5)
c = a / b

print(c.get_x())