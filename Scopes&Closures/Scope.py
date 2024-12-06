"""
Scoping
"""

a = 10
def func():
    print(a)

#python will look a inside scope of func(), if not found,
#will look up in module scope which also refered as global scope
#if there also won't found then built in scope 
# where built in funcs and values are defined
#so here a will be printed out as 10
func()
def func():
    print(a)
    a=20
#now if we look at this, we apparently find this as printing a as 10
#from module scope, and then assigning that a as 20
#but no it won't work like that, at compile time, function determines 
#it's scope, the variables inside that scope. so here, 
# a will be determined as local to function, and at runtimne it will give an error
#whil printing it
try:
    func()
except UnboundLocalError:
    print(UnboundLocalError)

def func(x):
    print(id(x))
    print(id(a))
    x/=2
    print(x)
func(a)
print(a)
#here if we look at memory address of a and x it will be same
#because function is having the access of global variable a here
#so changing x, would apperantly seen as changing global variable a
#but no, it won't change, and will be specific to that function scope, why?
#because integers are immutable
nums = [4,1,2,8,0]
def func(List):
    print(id(nums))
    print(id(List))
    List.sort()
    print(List)
func(nums)
print(nums)
#but this will affect the nums outside the function also
#because we are passing nums to function, is not just value, but memory address
#as in prev ex, memory address would be same for global nums and local List
#& so list are mutable it will be chganged.

#only way to change global immutables, is that defining global keyword
def func():
    global a
    a/=2
    print(a)
func()
print(a)
#this will change global value of a

a = 10
def outer_func():
    a = 100
    def inner_func():
        a=1000
        print(a)
    inner_func()
    print(a)

print(a) #global a =10
outer_func() #inner func scope a =1000, after print(a) will print local func a =100
print("<-!------------>")
a = 10
def outer_func():
    a = 100
    def inner_func1():
        nonlocal a 
        a=1000
        def inner_func2():
            nonlocal a 
            a=20
        print(f'a befor inner_func2: {a}')
        inner_func2()
        print(f'a after inner_func2: {a}')
    print(f'a befor inner_func1: {a}')
    inner_func1()
    print(f'a after inner_func1: {a}')

print(f'a befor outer_func: {a}')
outer_func()
print(f'a after outer_func: {a}')

#above example is how we can nest the nolocal variables
#but when we nest global variable in our local function,
#inner function of that, we can't nest that as nonlocal
#ex:
'''
a = 'python'
def outer():
    global a
    def inner():
        nonlocal a
'''     
#we can't do above, it will give error, global can't be accessed as non local 
 


