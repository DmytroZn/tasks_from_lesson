import shelve
import re
import time

class Registration:

    def __init__(self):
        self._user_name = 0
        self._user_login = 0
        self._user_password_1 = 0
        self._user_password_2 = 0

    def sign_up(self):
        with shelve.open('file_of_data') as f:
            while True:
                self._user_name = str(input('what is your name: '))
                if re.match(r'([a-zA-Z]+)\D', self._user_name):
                    break
                else:
                    print('\n' 'You should write only letters')
            while True:

                self._user_login = str(input('what is your login: '))
                if re.match(r'\D', self._user_login):             
                    if self._user_login in f:
                        print('\n' 'This is login basy, try again')
                    
                    else:
                        break
                else:
                    print('\n' 'Login sould be only letters')
                  
            while True:    
                self._user_password_1 = str(input('write your password: '))
                self._user_password_2 = str(input('write one more your password: '))
                if re.findall(r'([a-zA-Z]+)([0-9]+)', self._user_password_1):
                    if self._user_password_1 == self._user_password_2:
                        f[self._user_login] = [self._user_name, self._user_password_1, [f'{self._user_name}, you are registered - {time.ctime()}']]
                        f['Admin'] = ['Admin', 'admin123',  'Hello, you are administrator']
                        print(f'Hello {self._user_name}, you are registered')
                        break
                    else:
                        print('\n' 'You password should be the same')
                else:
                    print('\n' 'Password should has letters and numbers')


class Authorization(Registration):

    LIST_RE = []

    def log_in(self):

        with shelve.open('file_of_data') as f:
            while True:
                self._user_login = str(input('what is your login: '))

                if self._user_login not in f:
                    print('Your login not real, try again')
                else:
                    break

            while True:
                self._user_password_1 = str(input('write your password: '))
                if f[self._user_login][1] == self._user_password_1:
                    print(f'{f[self._user_login][0]}, You inside')
                    self.LIST_RE.insert(0, self._user_login)
                    try:
                        del self.LIST_RE[1]
                    except IndexError:
                        pass
                    break
                else:
                    print('Not correct password')
                
class Authorization_Admin(Authorization):

    def print_info(self):
        with shelve.open('file_of_data') as f:
            for k, v in f.items():
                print(k, v)

    
        
    # f['Admin'] = ['Admin', 'admin123',  'Hello, you are administrator']







    



class Posts:

    def create_post(self):
        lists_post = []
        w = str(input('Write something: '))
        lists_post.append(f'{w} - {time.ctime()}')
        return lists_post



class User(Authorization):

    def enter(self):
        self._a = '1 - sign_up'
        self._b = '2 - log_in'
        self._c = '3 - log in like admin'

        while True:
            print('\n'f'{self._a}, {self._b}')
            try:
                choice = int(input('write your choice: '))
            except ValueError:
                print('Write only \'1\' or \'2\'')
                choice = 0


            if choice == 1:
                Registration().sign_up()
            elif choice == 2:
                    Authorization().log_in()
                    print('\n'f'{self.LIST_RE[0]}, what would you like to do...?')
                    break
            
        self._a = '1 - create post'
        self._b = '2 - see post'
        self._c = '3 - log_out'
        while True:
            print('\n' f'{self._a}, {self._b}, {self._c}')
            try:
                choice = int(input('write your choice: '))
            except ValueError:
                print('Write only \'1\' or \'2\' or \'3\'')
                choice = 0
            
            if choice == 1:
                with shelve.open('file_of_data', 's') as f:
               

                    var_of_log = self.LIST_RE[0]
                    list_of_log = f[var_of_log]
                    a=Posts().create_post()
                    list_of_log.append(a)
                    f[var_of_log] = list_of_log
                    

                

            elif choice == 2:
                with shelve.open('file_of_data') as f:

                    # User().print_info()
                 
                    print( f[ self.LIST_RE[0] ] [2:] )
                

            elif choice == 3:
                break
                        






# Registration().sign_up()
# Authorization().print_info()
# Authorization().log_in()
# one = User()
# one.in_and_out()

class A():
    def do_food(self):
        while True:
            one = User()
            one.enter()


A().do_food()

# one = Authorization()
# one.enter()
# one._user_login
# one.