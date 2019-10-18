from threading import Thread
import threading
import time
import re 
import urllib.request

# task 1
# Create a decorator that will run the function in a separate thread. 
# The decorator should accept the following arguments: 
# name of the stream, whether the stream is a daemon.

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



# task 2
# Create a function that will download a file from the Internet via a link, 
# hang the created decorator on it. 
# Create a list of 10 links for downloading. 
# Create a list of threads, a separate thread, for each of the links. 
# Each stream should signal that it has started working and 
# by which link it works, it should also inform when the download is finished.
def my_decorator(name, is_daemon):

    def decoranor(func):
        
        def wrapper(*args, **kwargs):
            
            # print('thread started 1')
            time.sleep(0.5)
            t = Thread(target=func, name=name, args=args, daemon=is_daemon)
            t.start()
            # print(t.isDaemon())
            # print('Thread ended')
            
        return wrapper

    return decoranor


name_threads = ['thread_1', 'thread_2', 'thread_3', 'thread_4', 'thread_5', 
'thread_6', 'thread_7', 'thread_8', 'thread_9', 'thread_10']

for l in name_threads:
    @my_decorator(l, False)
    def downloader_func(url):
        result = re.split(r'/', url)
        name1 = result[-1]
        time.sleep(0.5)
        print(f'{threading.currentThread().getName()} - name')
        print(f'Beginning file download with: {url}') 
        if urllib.request.urlretrieve(url, f'{name1}.png'):
            print(f'end dowloaded {name1}')


list_of_url = ['http://i.stack.imgur.com/m3lqF.png',
'http://klike.net/uploads/posts/2018-08/1533804907_1.jpeg', 
'http://klike.net/uploads/posts/2018-08/medium/1533804949_5.jpg', 
'http://klike.net/uploads/posts/2018-08/1533804978_7.jpg', 
'http://klike.net/uploads/posts/2018-08/1533804939_11.jpg',
'http://techrocks.ru/wp-content/uploads/2018/11/python-is-the-best-programming-840x500.jpg',
'http://techrocks.ru/wp-content/uploads/2018/11/djangoproject.png',
'http://techrocks.ru/wp-content/uploads/2018/11/Flask.png',
'http://techrocks.ru/wp-content/uploads/2018/11/web2py.png',
'http://techrocks.ru/wp-content/uploads/2018/11/cherrypy-980x581.png'
]

for i in list_of_url:
    downloader_func(i)


# task 3
# Write your context manager for working with files.
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