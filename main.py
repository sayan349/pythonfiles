# This is a sample Python script.
def log(func):
    def wrapper(*args,**kwargs):
        print('i am logging')
        func(*args,**kwargs)
    return wrapper

def register(func):
    def inner(*args,**kwargs):
        print('i am registering')
        func(*args,**kwargs)
    return inner

@register
@log
def main(name,pwd):
    print(name,pwd)
main('sayan',123)