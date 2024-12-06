"""
clousers
"""

def outer():
    x = [1,2,3] 
    y=[4,5,6]                                            
    print(f'id of x (outer): {hex(id(x))}')
    print(f'id of y (outer): {hex(id(y))}')
    def inner():                                        #
        y = x #y reference to x outer local scope       #
        print(f'id of y (inner): {hex(id(y))}')                 #
    return inner

fn = outer() #this fn is clouser
#which has nested inner function, not just inner function
#but free variable x also. because, y in inner function has value of x
#which is nonlocal, in the scope outer func. 
#in inner functions, variables from outer scope/nonlocal
# are not directly refers to same object, but intermediatery cell generated
# both references to that cell, which references to object 
#here x and y will not reference directly to list [1,2,3] but to a cell, 
#which will reference to [1,2,3]. 
print(fn.__closure__) #see a cell adress would be visible
print(fn.__code__.co_freevars) #free variables are those which used in inner function 
#here in ex, x would be free variable. but not y. 
fn()

print('<--!------------->')

def pow(n):
    print(hex(id(n)))
    def num_to_pow_of(x):
        return n**x
    return num_to_pow_of

fn = pow(3)
print(fn.__closure__)
print(fn.__code__.co_freevars)
print(fn(2))

