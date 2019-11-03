from mongoengine import *
import datetime
connect('stud_db')



class Student(Document):
    first_name = StringField()
    last_name = StringField()
    groupe = StringField()
    marks = ListField()
    teacher = StringField()
    faculty = StringField()


class Machine():

    def create_stud(self):
        self._name = input('Write name: ')
        self._surname = input('Write surname: ')
        self._groupe = input('Write groupe: ')
        self._marks = input('Write marks: ')
        self._teacher = input('Write teacher for student: ')
        self._faculty = input('Write faculty: ')
    
        dict_stud_1 = {
            'first_name' : self._name,
            'last_name' : self._surname,
            'groupe' : self._groupe,
            'marks' : [self._marks],
            'teacher' : self._teacher,
            'faculty' : self._faculty
        }
        stud_1 = Student(**dict_stud_1).save()
        print('\n Student was added')

    def read_stud(self):
        u = Student.objects()
        for i in u:
            print(f'\n name student: {i.first_name} {i.last_name}; faculty: {i.faculty}; groupe: {i.groupe}; and teacher - {i.teacher};')
            for k in i.marks:
                print(f'marks: {k}')
                
    def update_stud(self):
        Machine().do_know()
        self._nam = input('Write name: ')
        self._sur = input('Write surname: ')

        print('''
        1 - Change name; 
        2 - Change surname; 
        3 - Change groupe;
        4 - Change faculty;
        5 - Change teacher ''')
        answ = int(input('What do you want to do? '))
        self._new_value = input('Write new: ')
        if answ == 1:
            stud_1 = Student.objects(first_name=self._nam, last_name=self._sur).update(first_name = self._new_value)
        elif answ == 2:
            stud_1 = Student.objects(first_name=self._nam, last_name=self._sur).update(last_name = self._new_value)
        elif answ == 3:
            stud_1 = Student.objects(first_name=self._nam, last_name=self._sur).update(groupe = self._new_value)
        elif answ == 4:
            stud_1 = Student.objects(first_name=self._nam, last_name=self._sur).update(faculty = self._new_value)
        elif answ == 5:
            stud_1 = Student.objects(first_name=self._nam, last_name=self._sur).update(teacher = self._new_value)
        print('Your change was updated')

    def delete_stud(self):
        Machine().do_know()
        self._nam = input('Write name: ')
        self._sur = input('Write surname: ')
        stud_1 = Student.objects(first_name=self._nam, last_name=self._sur).delete()
        print('Student was deleted')



    def do_know(self):
        print('Do you know student? (y/n)')
        while True:
            answ = input()
            if answ == 'n':
                stud_1 = Student.objects()
                for i in stud_1:
                    print(i.first_name, i.last_name)
                print()
                break
            elif answ == 'y':
                break
            else:
                print('Not correct answer, write y or n')
        
       

    def read_stud_of_teacher(self):
        print('Do you know teachers? (y/n)')
        while True:
            answ = input()
            if answ == 'n':
                stud_1 = Student.objects()
                for i in stud_1:
                    print(i.teacher)
                print()
                break
            elif answ == 'y':
                break
            else:
                print('Not correct answer, write y or n')

        self._teach = str(input('Write name`s teacher: '))
        stud_1 = Student.objects()
        print('Students which have the same teacher:')
        for i in stud_1:   
            if i.teacher == self._teach:
                print(i.first_name, i.last_name)
        

# {'first_name_surname' : 'Dmytro Znak'}
# stud_1 = Student().find()
# db.Student.find()
# u = Student.objects(first_name_surname = 'Dmytro Znak').first()
# print(u)

def ma():
    while True:
        print('''
        1 - Add student;
        2 - See all students;
        3 - Update something;
        4 - Delete student;
        5 - See students which have the same teacher
        ''')
        answ = int(input('What do you want? '))
        if answ == 1:
            Machine().create_stud()
        elif answ == 2:
            Machine().read_stud()
        elif answ == 3:
            Machine().update_stud()
        elif answ == 4:
            Machine().delete_stud()
        elif answ == 5:
            Machine().read_stud_of_teacher()

# Machine().create_stud()
# Machine().read_stud()
# Machine().update_stud()
# Machine().do_know()
# Machine().delete_stud()
# Machine().read_stud_of_teacher()

ma()
# u = Student.objects()


    # print({i.marks})
# print(u.to_json())

# p = u.to_json()



