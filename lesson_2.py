# Create a class car. Describe common attributes. 
# Create passenger car and truck classes. 
# Describe basic attributes for cars in the main class.
# It will be a plus if you override the methods of the base class in the heir classes.
class Car:

    def move(self):
        return 'Car drives'

    def add_fuel(self, value):
        self._fuel += value

    def get_fuel(self):
        return self._fuel

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        self._brand = value

    def get_engine(self):
        return self._engine

    def set_engine(self, value):
        self._engine = value

    def __str__(self):
        return f'Brand is {self._brand} and engine is {self._engine}'
    
    def get_way(self):
        return f'{self._way} km'
    
    def set_way(self, value):
        self._way = value

    def get_car_release(self):
        return self._car_release
    
    def set_car_release(self, value):
        self._car_release = value


class Truck(Car):

    def __init__(self, fuel, brand, engine, way, car_release, bag):
        self._fuel = fuel
        self._brand = brand
        self._engine = engine
        self._way = way
        self._car_release = car_release
        self._bag = bag
        

    def move(self):
        return 'Truck drives'
    
    def get_way(self):
        return f'Truck drove througt {self._way} km'

    def get_bag(self):
        return f'Truck delivers {self._bag} bag' if self._bag == 1 else f'Truck delivers {self._bag} bags'

    def set_bag(self, value):
        self._bag = value


class PassengerCar(Car):

    def __init__(self, fuel, brand, engine, way, car_release):
        self._fuel = fuel
        self._brand = brand
        self._engine = engine
        self._way = way
        self._car_release = car_release
    
    def move(self):
        return 'Passenger car drives'
    
    def get_way(self):
        return f'Passenger car drove througt {self._way} km'
    

# truck1 = Truck(0, 'Mercedes', 'GR215', 200, 2017, 15)
# passenger_car1 = PassengerCar(0, 'Lexus', 'L20', 210, 2019)

# print(truck1.get_bag())
# truck1.set_bag(17)
# print(truck1.get_bag())

# print(truck1.move())
# print(passenger_car1.move())



# Create a store class. 
# The designer must initialize the values: 
# "Store Names" and "Number of Items Sold". 
# Implement object methods that will increase the number of goods sold, 
# and implement the output of a class variable value that will store 
# the total number of goods sold by all stores.
class Store:

    AMOUNT_SOLD_OUT_ALL_SHOPS = 0

    def __init__(self, name, count_sold_out):
        self._name = name 
        self._count_sold_out = count_sold_out
        Store.AMOUNT_SOLD_OUT_ALL_SHOPS += count_sold_out
    
    def add_count_sold_out(self, value):
        self._count_sold_out += value

    def get_count_sold_out(self):
        return f'Sold out products are {self._count_sold_out} amount in {self._name}'

    def count_sold_out_all_shops(self):
        return AMOUNT_SOLD_OUT_ALL_SHOPS
    

ashan = Store('Ashan', 12)
atb = Store('ATB', 100)

# print(ashan.get_count_sold_out())
ashan.add_count_sold_out(122)
# print(ashan.get_count_sold_out())

# print(atb.get_count_sold_out())
# print(ashan.AMOUNT_SOLD_OUT_ALL_SHOPS)



# Create a point class, implement a constructor 
# that initializes 3 coordinates (x, y, z). 
# Implement methods for getting and changing each coordinate. 
# Overload for this class the methods of addition, subtraction, 
# division of multiplication.
# Overload one any unary method.
# Expected result: I multiply the point with coordinates 1, 2, 3 
# by another point with the same coordinates, I get the result 1, 4, 9.

class Point:
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def add_x(self, value):
        self._x = value
    
    def get_x(self):
        return self._x
    
    def add_y(self, value):
        self._y = value
    
    def get_y(self):
        return self._y

    def add_z(self, value):
        self._z = value
    
    def get_z(self):
        return self._z


    def get_points(self):
        return self._x, self._y, self._z

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y, self._z + other._z)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y, self._z - other._z)

    def __mul__(self, other):
        return Point(self._x * other._x, self._y * other._y, self._z * other._z)

    def __truediv__(self, other):
        return Point(self._x / other._x, self._y / other._y, self._z / other._z)

    def __floordiv__(self, other):
        return Point(self._x // other._x, self._y // other._y, self._z // other._z)
         
    def __mod__(self, other):
        return Point(self._x % other._x, self._y % other._y, self._z % other._z)

    def __and__(self, other):
        return Point(self._x & other._y, self._y & other._y, self._z & other._z)



a = Point(1, 2, 3)
b = Point(2, 5, 6)

a.add_x(5)

print(a._x)
print(a.get_x())

c = a * b
print(c.get_points())

    