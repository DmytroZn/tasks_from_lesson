from threading import Thread
import threading
import time
import re 
import urllib.request

# task 1

def simple_decorator(name, is_daemon):

    def decoranor(func):
        
        def wrapper(*args, **kwargs):
            print('thread started 1')
            time.sleep(0.5)
            t = Thread(target=func, args=(5, ), name=name, daemon=is_daemon)
            t.start()
            print('thread ended 2')
            print(t.isDaemon())

        return wrapper

    return decoranor

@simple_decorator('Thread_1', False)
def random_time_sleep(time_to_sleep):
    print('thread started')
    print('thread ended')

# random_time_sleep(2)

# print('Main thred process ...')

# for _ in range(10):
#     print('works')
#     print('Iteration ended')



# # task 2

def my_decorator(is_daemon):

    def decoranor(func):
        
        def wrapper(*args, **kwargs):
            
            # print('thread started 1')
            time.sleep(0.5)

            t = Thread(target=func, args=args, daemon=is_daemon)
            t.start()
            # print(t.isDaemon())
            # print('Thread ended')
            

        return wrapper

    return decoranor




@my_decorator(False)
def downloader_func(url):
    result = re.split(r'/', url)
    name1 = result[-1]
    time.sleep(0.5)
    print(f'{threading.currentThread().getName()} - name')
    print(f'Beginning file download with {url}') 
    if urllib.request.urlretrieve(url, f'{name1}.png'):
        print('end dowloaded')



list_of_url = ['http://i.stack.imgur.com/m3lqF.png',
'http://klike.net/uploads/posts/2018-08/1533804907_1.jpeg', 
'http://klike.net/uploads/posts/2018-08/medium/1533804949_5.jpg', 
'http://klike.net/uploads/posts/2018-08/1533804978_7.jpg', 
'http://klike.net/uploads/posts/2018-08/1533804939_11.jpg'
]



for i in list_of_url:
    downloader_func(i)
# for i in enumerate(list_of_url):
#     downloader_func(i, i)

#########################################################################


# task 3

class ContextOpen:


    def __init__(self, name_file, method):
        self._name_file = name_file
        self._method = method
        self._state = 'Active'
        self._open_file = open(self._name_file, self._method)

    def __enter__(self):
        print('Open file')
        return self._open_file

    def __exit__(self,  exc_type, exc_val, et_tb):
        self._state = 'Inactive'
        self._open_file.close()
        print('Closed file')
      

# with ContextOpen('file.txt', 'w') as y:
#     y.write('sdfsdf')

# with ContextOpen('file.txt', 'r') as y:
#     print(y.read(1))

# with open('file.txt', 'r') as r:
#     print(r.read(1))