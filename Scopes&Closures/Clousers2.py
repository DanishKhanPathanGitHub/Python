#an avrager function with object oriented programming
#vs functional - clouser:
class AvragerClass():
    
    def __init__(self):
        self.total = 0
        self.count = 0
    
    def add(self, number):
        self.total+=number
        self.count+=1
        print(self.total/self.count)
    
print("With class:----------")
a = AvragerClass()
a.add(10)
a.add(20)
a.add(30)

def AvragerClouser():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total+=number
        count+=1
        print(total / count)
    return add
print("With clouser:----------")
a = AvragerClouser()
a(10)
a(20)
a(30)
print('<--!----function run counter----------->')

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

def subtract(a, b):
    return a-b

counter_add = counter(add)
counter_subtract = counter(subtract)

print('clouser of counter function: ', counter_add.__closure__)
print('free vars of counter', counter_add.__code__.co_freevars)

for i in range(1,6):
    counter_add(i)
#this will print add has been ran 5 times and result of add func
