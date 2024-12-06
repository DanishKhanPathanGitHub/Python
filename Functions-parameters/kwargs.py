def fun(a,*b, c):
    print(a)
    print(b)
    print(c)
try:
    print(fun(1,2,3,4))
except:
    print('positional arguments must be followed by keyword argument')
    print(fun(1,2,3,c=4))


def fun1(*, a):
    print("this function won't allow any positional arguments")
    print(a)

try:
    print(fun1(1,2, a=2))
except:
    print(fun1(a=2))

def fun2(a,b=2,*c,d=2,e):
    print(a,b,c,d,e)
#important notes here:
#b is default keyword argument
#a is mendatory positinal argument, as b is optional kwarg, set to default 
# and *c is optional positional args
#all arguments followed by *c are keyword arguments
#d is default keyword argument set to 2, so optional, and e is mendatory kwarg
fun2(1,32,e=2)
#a=1, b=32, *c is optional so empty tuple, d=2 as default, e=2
#but what if we wanted to assign 32 to args not to b, as b is set to default
#we want to keep as it is,
#because even if b=2 is keyword argument, it acts as positional,
#because it comes before other positional args like *c here.
#so if we do like this: fun2(1,32,e=2,b=3), it won't work
#32 assigned to b, and at the end we re assign b=3, so error will be...
#got multiple values of b
#so every argument, keyyword or not, which comes before actual positional *args
#like *, or **kwargs which means now all args will be considered as keword args
#before that all will be act as positional
fun2(1,2,32,34,e=100,d=200) 
#See the program of Function introspection
