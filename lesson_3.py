import time

# Create a decorator with arguments. 
# Which will call a function a certain number of times, 
# it will output the amount of time spent to perform 
# this function and its name.

def my_decorator(num=1):

    def decorator(func):

        def wraper(*args, **kwargs):
            list_of_already = []
            start_time = time.time()
            dict_of_val = {}
            list_of_func = []
            for i in range(num):
                dict_of_val['time'] = f'{time.time() - start_time} sec'
                dict_of_val['name of function'] = func.__name__
                dict_of_val['out put'] = func(*args, **kwargs)
                list_of_already.append(dict_of_val)  
                print(dict_of_val)
            
            
        return wraper  

    return decorator

@my_decorator(4)
def say_hello(name):
    return f'hello {name}'

print(say_hello('Dima'))




# def my_decorator(num=1):

#     def decorator(func):
        

#         def wraper(*args, **kwargs):
#             list_of_already = []
#             n = 1
#             start_time = time.time()
#             while num >= n:
#                 dict_of_val = {}
#                 list_of_func = []
#                 for i in range(n):
#                     list_of_func.append(func(*args, **kwargs))
#                 dict_of_val['name of function'] = func.__name__
#                 dict_of_val['out put'] = list_of_func
#                 dict_of_val['time'] = f'{time.time() - start_time} sec'
#                 list_of_already.append(dict_of_val)  
#                 n += 1    
                        
#             return list_of_already

#         return wraper  

#     return decorator

# @my_decorator(4)
# def say_hello(name):
#     return f'hello {name}'

# print(say_hello('Dima'))




