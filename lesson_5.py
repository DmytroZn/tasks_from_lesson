from threading import Thread
import time

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



# task 2

def my_decorator(name, is_daemon):

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



list_of_name_threads = ['thread_1', 'thread_2', 'thread_3', 'thread_4', 'thread_5', 'thread_6'] 



# for i in list_of_name_threads:
#     @my_decorator(i, False)
#     def downloader_func(url, name1):
#         print('Beginning file download with urllib2...')
#         return urllib.request.urlretrieve(url, f'{name1}.png')

@my_decorator('sdf', False)
def downloader_func(url, name1):
    print('Beginning file download with urllib2...')
    return urllib.request.urlretrieve(url, f'{name1}.png')



list_of_url = ['http://i.stack.imgur.com/m3lqF.png', 
'http://i.stack.imgur.com/m3lqF.png', 
'http://klike.net/uploads/posts/2018-08/1533804907_1.jpeg', 
'http://klike.net/uploads/posts/2018-08/medium/1533804949_5.jpg', 
'http://klike.net/uploads/posts/2018-08/1533804978_7.jpg', 
'http://klike.net/uploads/posts/2018-08/1533804939_11.jpg'
]
list_of_name_files = [1, 2, 3, 4, 5, 6]



for i, k in zip(list_of_url, list_of_name_files):
    downloader_func(i, k)
    


url = 'http://klike.net/uploads/posts/2018-08/1533804939_11.jpg'  

# downloader_func(url, 'some_name')
