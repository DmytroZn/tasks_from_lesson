import sqlite3

# name = input('write name: ')
# faculty = input('Write faculty: ')
# groupe = input('write groupe: ')
# number_stud = input('write number of student`s ticket')
# mark = input('write mark: ')



# conn = sqlite3.connect('student.db')
# cursor = conn.cursor()

# query_response = cursor.execute('SELECT * FROM student')

# # print(query_response)
# print(query_response.fetchall())
# # print(query_response.fetchone())
# a = cursor.execute("""SELECT * FROM student INNER JOIN role
# on student.role_id = role.id""")

# print()
# print(a.fetchall())



# conn.close()


class Administrator:

    def __init__(self):
        self._conn = sqlite3.connect('lesson_7.db')
        self._cursor = self._conn.cursor()



    def add_student(self):
        while True:
            self._name = str(input('write name: '))

            self._sql = f"""SELECT name FROM student WHERE name = '{self._name}' """
            self._sql = self._cursor.execute(self._sql)
            self._num = self._sql.fetchone()
 
            if self._num == None:
                break
            else:
                print('That name is busy, create not same')
    


        self._faculty = input('Write faculty: ')
        self._groupe = input('write groupe: ')
        while True:
            self._number_stud = input('write number of student`s ticket: ')
            self._sql = f"""SELECT number_stud FROM data_stud WHERE number_stud = '{self._number_stud}' """
            self._sql = self._cursor.execute(self._sql)
            self._num = self._sql.fetchone()
 
            if self._num == None:
                break
            else:
                print('That number is busy, create not same')
  

        self._sql = """INSERT INTO student (name) VALUES(?) """
        self._query_response = self._cursor.execute(self._sql, [self._name])

        self._sql = f"""SELECT id FROM student WHERE name='{self._name}'"""
        self._sql = self._cursor.execute(self._sql)
        self._num = self._sql.fetchone()[0]
        
        self._sql = """INSERT INTO data_stud (id_student, faculty, groupe, number_stud) VALUES(?, ?, ?, ?) """
        self._query_response = self._cursor.execute(self._sql, [self._num, self._faculty, self._groupe, self._number_stud])

        self._conn.commit()
        self._conn.close()
        print('\n Student was added \n')

    def add_mark_subject(self):
        while True:
            try:
                self._ques_1 = input('Do you know student which you want to add mark? \n (YES or No: y/n)\n')
            except (KeyboardInterrupt, AttributeError):
                self._ques_1 = 0
                print('\n Write only \'y\' or \'n\' ')
                
            if self._ques_1 == 'n':
                self._sql = """SELECT name FROM student """
                self._sql = self._cursor.execute(self._sql)
                for i in self._sql.fetchall():
                    print(i[0])
                break
            elif self._ques_1 == 'y':
                break
            else:
                print('Try again, not correct answer')


        while True:
           
            try:
                self._ques_2 = input('\n Which student do you want to add mark?\n')
            except (TypeError,KeyboardInterrupt):
                self._ques_2 = 'None'
            self._sql = f"""SELECT name FROM student WHERE name = '{self._ques_2}' """
            self._sql = self._cursor.execute(self._sql)
            if self._sql.fetchall() == []:
                print('Not real student, try again')
        
            else:
                break


 
        self._sql = """SELECT title FROM subject """
        self._sql = self._cursor.execute(self._sql)
        print()
        for i in self._sql.fetchall():
            print(i[0])

        while True:
            try:
                self._ques_3 = input('\n Which subject do you want to use?\n')
            except (KeyboardInterrupt, AttributeError):
                self._ques_3 = 'None'
                print('Try again')
                pass
            self._sql = f"""SELECT title FROM subject WHERE title = '{self._ques_3}' """
            self._sql = self._cursor.execute(self._sql)
            if self._sql.fetchall() == []:
                print('Not real subject, try again')
            else:
                break

        if self._ques_3 == 'IT':
            self._subject = 1
        elif self._ques_3 == 'Chemistry':
            self._subject = 2
        elif self._ques_3 == 'Math':
            self._subject = 3

        self._sql = f"""SELECT id FROM student WHERE name = '{self._ques_2}' """
        self._sql = self._cursor.execute(self._sql)
        self._num = self._sql.fetchone()[0]


        while True:
            try:
                self._mark = int(input('write mark: '))
            except ValueError:
                self._mark = -1
            if 0 <= self._mark <= 5:
                break
            else:
                print('\n Mark should be only from 0 to 5 points')

        self._sql = """INSERT INTO mark_of (mark, id_subject, id_student) VALUES(?, ?, ?) """
        self._query_response = self._cursor.execute(self._sql, [self._mark, self._subject, self._num])

        self._conn.commit()
        self._conn.close()
        print('Student got a mark')

    def update_student(self):

        while True:
            try:
                self._ques_1 = input('Do you know student which you want to change? \n (YES or No: y/n)\n')
            except (KeyboardInterrupt, AttributeError):
                self._ques_1 = 0
                print('\n Write only \'y\' or \'n\' ')
                
            if self._ques_1 == 'n':
                self._sql = """SELECT name FROM student """
                self._sql = self._cursor.execute(self._sql)
                for i in self._sql.fetchall():
                    print(i[0])
                break
            elif self._ques_1 == 'y':
                break
            else:
                print('Try again, not correct answer')





        while True:
           
            try:
                self._ques_2 = input('\n Which student do you want to change?\n')
            except (TypeError,KeyboardInterrupt):
                self._ques_2 = 'None'
            self._sql = f"""SELECT name FROM student WHERE name = '{self._ques_2}' """
            self._sql = self._cursor.execute(self._sql)
            if self._sql.fetchall() == []:
                print('Not real student, try again')
            else:
                break
        
        print(self._ques_2)

        self._list_to_change = ['\n', 'name', 'faculty', 'groupe', 'number of student`s tickets']
        
        for i in self._list_to_change:
            print(i)    
        
        while True:
            try:
                self._ques_4 = input('\n What do you want to change?\n')
            except (TypeError,KeyboardInterrupt):
                self._ques_4 = 'None'

            if self._ques_4 not in self._list_to_change:
                print('Try again, that was not real variable')
            else:
                break

        while True:

            if self._ques_4 == 'name':
                try:
                    self._ques_5 = str(input('What is new name: '))
                except (TypeError,KeyboardInterrupt):
                    print('Don`t save name, try again')
                    break
                self._sql = f"""UPDATE student SET name = '{self._ques_5}' WHERE name = '{self._ques_2}' """
                self._sql = self._cursor.execute(self._sql)
                self._conn.commit()
                self._conn.close()
                print('Name was changed')
                break

            elif self._ques_4 == 'faculty':
                try:
                    self._ques_5 = str(input('What is new faculty: '))
                except (TypeError,KeyboardInterrupt):
                    print('\n Don`t save faculty, try again')
                    break
                self._sql = f"""SELECT id FROM student WHERE name = '{self._ques_2}' """
                self._sql = self._cursor.execute(self._sql)
                self._id = self._sql.fetchone()[0]
                self._sql = f"""UPDATE data_stud SET faculty = '{self._ques_5}' WHERE id_student = '{self._id}' """
                self._cursor.execute(self._sql)
                self._conn.commit()
                self._conn.close()
                print('Faculty was changed')
                break

            elif self._ques_4 == 'groupe':
                try: 
                    self._ques_5 = str(input('What is the new groupe: '))
                except (TypeError,KeyboardInterrupt):
                    print('\n Don`t save groupe, try again')
                    break

                self._sql = f"""SELECT id FROM student WHERE name = '{self._ques_2}' """
                self._sql = self._cursor.execute(self._sql)
                self._id = self._sql.fetchone()[0]
                self._sql = f"""UPDATE data_stud SET groupe = '{self._ques_5}' WHERE id_student = '{self._id}' """
                self._cursor.execute(self._sql)
                self._conn.commit()
                self._conn.close()
                print('Groupe was changed')
                break

            elif self._ques_4 == 'number of student`s tickets':
                try:
                    self._ques_5 = str(input('What is the new number: '))
                except (TypeError,KeyboardInterrupt):
                    print('\n Don`t save number, try again')
                    break
                self._sql = f"""SELECT id FROM student WHERE name = '{self._ques_2}' """
                self._sql = self._cursor.execute(self._sql)
                self._id = self._sql.fetchone()[0]
                self._sql = f"""UPDATE data_stud SET number_stud = '{self._ques_5}' WHERE id_student = '{self._id}' """
                self._cursor.execute(self._sql)
                self._conn.commit()
                self._conn.close()
                print('Number of student`s tickets was changed')
                break


class Student:

    def __init__(self):
        self._conn = sqlite3.connect('lesson_7.db')
        self._cursor = self._conn.cursor()

    def get_info_one_stud(self):

        while True:
            try:
                self._ques_1 = input('Do you know student which you want to add mark? \n (YES or No: y/n)\n')
            except (KeyboardInterrupt, AttributeError):
                self._ques_1 = 0
                print('\n Write only \'y\' or \'n\' ')
                
            if self._ques_1 == 'n':
                self._sql = """SELECT name FROM student """
                self._sql = self._cursor.execute(self._sql)
                for i in self._sql.fetchall():
                    print(i[0])
                break
            elif self._ques_1 == 'y':
                break
            else:
                print('Try again, not correct answer')


        while True:
           
            try:
                self._ques_2 = input('\n Which student do you want to know information?\n')
            except (TypeError,KeyboardInterrupt):
                self._ques_2 = 'None'
            self._sql = f"""SELECT name FROM student WHERE name = '{self._ques_2}' """
            self._sql = self._cursor.execute(self._sql)
            if self._sql.fetchall() == []:
                print('Not real student, try again')
        
            else:
                break
        
        self._sql = f""" 
        SELECT name, mark, title, faculty, groupe, number_stud FROM data_stud
        INNER JOIN student
        on data_stud.id_student=student.id
        INNER JOIN mark_of
        on student.id=mark_of.id_student
        
        INNER JOIN subject
        on mark_of.id_subject=subject.id
        WHERE name='{self._ques_2}'
        """
        self._sql = self._cursor.execute(self._sql)
        
        List_info = self._sql.fetchall()
        len_list = len(List_info)
        k = f"""name: {List_info[0][0]}; faculty: {List_info[0][3]}; groupe: {List_info[0][4]}; number student`s ticket: {List_info[0][5]}; """
        print(k)
        print('\a\tsubject : marks ')
        for i in range(len_list): 
            print(f"""\t\b\b\b{List_info[i][2]} \t:   {List_info[i][1]}""")

    def find_student(self):
        pass

#         SELECT name, mark, title, faculty, groupe, number_stud FROM data_stud
# INNER JOIN student
# on data_stud.id_student=student.id
# INNER JOIN mark_of
# on student.id=mark_of.id_student
# INNER JOIN subject
# on mark_of.id_subject=subject.id
# WHERE name='Dima Znak'

            


        # self._sql = """INSERT INTO mark_of (mark, subject, id_student) VALUES(?, ?, ?) """
        # self._query_response = self._cursor.execute(self._sql, [self._mark, ])

            

        
            
            

        # self._mark = input('write mark: ')
        # self._sql = """INSERT INTO mark_of (id_student) VALUES(?) """
        # self._query_response = self._cursos.execute(self._sql, [])
        # pass

    

class Machine:
    def start(self):
        self._q = """
        \n 
        1 - Add new student; 
        2 - Add mark for student; 
        3 - Update student`s date; 
        4 - Log_out; \n
        """
        self._r = """
        \n 
        1 - Get list of the best students; 
        2 - Get list of the all students; 
        3 - Find student for his student`s tickets; 
        4 - Get information about student; 
        5 - Log out; \n
        """
        while True:   
            print('\n 1 - Administrator', '\n', '2 - Student \n')
            try:
                self._user = int(input('\n Who are you? '))
            except (ValueError, AttributeError, KeyboardInterrupt):
                print('\n Write only \'1\' or \'2\' ')
                self._user = 0

            if self._user == 1:
                while True:
                    print(self._q)
                    try:
                        self._b = int(input('\n What do you want to do? '))
                    except (ValueError, KeyboardInterrupt, AttributeError):
                        print('\n Write only \'1\' or \'2\' or \'3\' or \'4\'')
                        self._b = 0

                    if self._b == 1:
                        Administrator().add_student()
                    elif self._b == 2:
                        Administrator().add_mark_subject()
                    elif self._b == 3:
                        Administrator().update_student()
                    elif self._b == 4:
                        break
                    
                    
            elif self._user == 2:
                while True:
                    print(self._r)
                    try:
                        self._d = int(input('\n What do you want to do? '))
                    except (ValueError, KeyboardInterrupt, AttributeError):
                        print('\n Write only \'1\' or \'2\' or \'3\' or \'4\'')
                        self._b = 0

                    if self._d == 1:
                        pass

                    elif self._d == 2:
                        pass

                    elif self._d == 3:
                        pass

                    elif self._d == 4:
                        Student().get_info_one_stud()

                    elif self._d == 5:
                        break

                # print('Student not ready, sorry')
           
                        
                    
                # Administrator().add_student()
                # Administrator().add_mark_subject()
                # Administrator().update_student()
a = Machine()
a.start()