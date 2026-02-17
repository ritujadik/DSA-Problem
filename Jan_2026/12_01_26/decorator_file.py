def log_calls(func):
    log = {'count':0}

    def wrapper(*args,**kwargs):
        log['count'] +=1
        print(f"function '{func.__name__}' called {log['count']} times")
        return func(*args,**kwargs)

    wrapper.log = log
    return wrapper


@log_calls
def greet(name):
    print(f"hello,{name}")

greet("alice")
greet("ritu")