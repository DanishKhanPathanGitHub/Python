def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print(f'{fn.__name__} has been run {count} times')
        return fn(*args, **kwargs)
    return inner

@counter
def add(a: int, b: int =0) ->int:
    """
    Will add two numbers and returns result
    one parameter is optional set to 0
    """
    print(a+b)
    return a+b

print(help(add))
#This won't show the docstring and param types of the add func
#but will show the inner func output of help, becuase now, 
# add decorated by the counter, which is now pointing to inner func, not add
#so we can manually set up the docstring of actual func rathern than inner
#but we have functool module which take care of that task
from functools import wraps

def counter2(fn):
    count = 0
    @wraps(fn)
    #or inner = wrap(fn)(inner)
    #wrap is itself a decorator
    #this will wrap the inner function by fn,
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print(f'{fn.__name__} has been run {count} times')
        return fn(*args, **kwargs)
    return inner

@counter2
def add2(a: int, b: int =0) ->int:
    """
    Will add two numbers and returns result
    one parameter is optional set to 0
    """
    print(a+b)
    return a+b

print(help(add2))