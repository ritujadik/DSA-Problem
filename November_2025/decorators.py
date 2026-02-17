# what is decorators.with the real life example
#Answer: decorators are the special type of function which takes the another function as an parameter and add the value in their behaviour
# without changing their orignal behaviour.
# we use @ prefix to denote the decorator
import datetime
def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time = datetime.datetime.now()
        result = func(*args,**kwargs)
        end_time = datetime.datetime.now()
        print("execution time :",end_time-start_time)
        return result
    return wrapper

@execution_time
def read_file(filename):
    with open(filename,'r') as f:
        data = f.read()
    print("file read successfully")
    return data


read_file("shallow_deep.py")
