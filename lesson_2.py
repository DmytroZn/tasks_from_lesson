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
    


truck1 = Truck(0, 'Mercedes', 'GR215', 200, 2017, 15)
passenger_car1 = PassengerCar(0, 'Lexus', 'L20', 210, 2019)

print(truck1.get_bag())
truck1.set_bag(17)
print(truck1.get_bag())

print(truck1.move())
print(passenger_car1.move())

