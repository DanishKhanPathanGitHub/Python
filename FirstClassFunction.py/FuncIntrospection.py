import inspect
import math
#TODO: to do this task use this function
def fun(a,
        b=2,
        c=3, 
        *args,
        d1=2, d2=3,
        e,
        **kwargs
    ):
    "this is docstring of fun" 
    print(a,b,c,d1,d2,e, kwargs)

print(fun.__annotations__)
print(fun.__doc__)
print(fun.__name__)
print(fun.__code__)
print(inspect.getcomments(fun))
#This will pick up the comments attatched before the function as #TODO 
print(inspect.getmodule(math.sqrt)) #will get the module where the function is defined
print('<-!----------------argument types------->')
print(fun.__defaults__)
print(fun.__kwdefaults__)
for param in inspect.signature(fun).parameters.values():
    print(f'{param.name}, type:{param.kind}')
#This will clear up the confusion of parameters type. there is also one more type
#parameter which is positional only
print("<-!---Types of parameters of divmod function----->")
for param in inspect.signature(divmod).parameters.values():
    print(f'{param.name}, type:{param.kind}')

#That means we cannot do divmod(x=2, y=4), no they are positional only
