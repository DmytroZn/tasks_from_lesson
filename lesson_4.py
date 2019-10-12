# Create a Person class with abstract methods that allow you to display 
# information about a person and also determine her age (in the current year). 
# Create child classes: Entrant (last name, date of birth, faculty), 
# Student (last name, date of birth, faculty, course), 
# Teacher (last name, date of birth, faculty, position, experience), 
# with your own methods for displaying information on the screen and determining age. 
# Create a list of n people, display the full information from the database on the screen, 
# and organize a search for people whose age falls into the given range.

from abc import ABC,abstractmethod
import datetime


class Person(ABC):

    d = datetime.date.today()
    NOW_YEAR = d.year

    def __init__(self, first_name, last_name, date_year):
        self._first_name = first_name
        self._last_name = last_name
        self._date_year = date_year

    # @abstractmethod
    def view_year(self):
        self._NOW_YEAR = 2019
        return (self._NOW_YEAR - self._date_year)
    
    @abstractmethod
    def get_person(self):
        return f'first name: {self._first_name}, last name: {self._last_name}, date: {view_year()}'


class Entrant(Person):
    
    def __init__(self, last_name, date_year, faculty):
        self._last_name = last_name
        self._date_year = date_year
        self._faculty = faculty

    @property
    def get_person(self):
        return f'last name: {self._last_name}, age: {self.view_year()}, faculty: {self._faculty}'
    
    def view_year(self):
        d = datetime.date.today()
        self._NOW_YEAR = d.year
        return (self._NOW_YEAR - self._date_year)


class Student(Person):

    def __init__(self, last_name, date_year, faculty, cours):
        self._last_name = last_name
        self._date_year = date_year
        self._faculty = faculty
        self._cours = cours

    @property
    def get_person(self):
        return f'Surname of student is {self._last_name}, his or her age: {self.view_year()}, faculty: {self._faculty}, cours: {self._cours}'


class Teacher(Person):

    def __init__(self, last_name, date_year, faculty, position, experience):
        self._last_name = last_name
        self._date_year = date_year
        self._faculty = faculty
        self._position = position
        self._experience = experience

    @property
    def get_person(self):
       return f'Surname of teacher is {self._last_name}, his or her age: {self.view_year()}, He or She works {self._position} on \'{self._faculty}\' faculty and has experience at work {self._experience} years'

entrant1 = Entrant('Znak', 1994, 'CTF')
student1 = Student('Klimko', 1994, 'CTF', 6)
entrant2 = Entrant('Dimkov', 1869, 'KJF')
teacher1 = Teacher('Doncova', 1986, 'Chemical tehnology', 'docent', 5)
n = [entrant1, entrant2, student1, teacher1]

for i in n:
    print(i.get_person)

range_of_age_1 = 20
range_of_age_2 = 30

list_already = []
for i in n:
    for k in range(range_of_age_1, range_of_age_2):
        if k == i.view_year():
            list_already.append(i._last_name)

print(f'There are persons have the same age : {list_already}')



