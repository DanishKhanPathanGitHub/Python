#decorator is a function which takes a function as argument and return a clouser
#remember wwhat we have done in clouser2.py file, in counter function
#look one more time:
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print(f'{fn.__name__} has been run {count} times')
        return fn(*args, **kwargs)
    return inner

def add(a, b=0):
    print(a+b)
    return a+b

#here counter takes a fn as argument, and return clouser-> inner func, here add
#so we decorated add func with counter func.
#this  above func and below code wrapping it by counter, to decorate it:
add = counter(add)
add(10,  11)
#is same as below code:
@counter
def mult(a, b=1):
    print(a*b)
    return a*b
#this is just syntax, all it does is, counter takes mult as parameter,
#and returns clouser of it
print(mult.__name__)
#this will/but shouldn't surprise you that, it will print inner, not mult
#because when we decorate the any func(here mult) via another func(here counter)
#it (mult) will point to the clouser func of the decorator func(here which is inner)
#this can be a problem at debugging, or at visualization of code
#which can be solved by functool module python provides. 
#before that we can partially change it manually
def counter2(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print(f'{fn.__name__} has been run {count} times')
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    #here we modified behaviour manually
    return inner

@counter2
def mult2(a, b=0):
    print(a*b)
    return a*b
print(mult2.__name__)
#in next decorator code ffile we will se functools...