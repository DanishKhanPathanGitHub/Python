from functools import partial

#before we use partial, we will write basic functionalities of partial manually
#partial allows to call a function ignoring some params

def func(x, y, z):
    return x+y+z

def partial_funct(a,b):
    return func(10, a, b)

#partial funct defined x as 10, so now we can call func 
#without passing all params, by calling partial_func
print(partial_funct(3,4)) #10+3+4

f = partial(func, 10)
print(f(10,20)) #10+10+20

#practical use case
def power(base, exponent):
    return base**exponent

sq = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(sq(6))
print(cube(6))
print(cube(6, exponent=2)) #we can still override behaviour of partial

Points = [(4,-5), (2,7), (0,-1), (6, -2)]

print(sorted(Points, key=lambda x: (x[0]-0)**2 + (x[1]-0)**2))
#basically what we did here, is, sorted points based on
#their distance from point (0,0)
#below how we can do with partial
f = lambda x, y: (x[0]-y[0])**2 + (x[1]-y[1])**2
#here we can make y as optional set to (0,0) and fking do all unnecessary things
#Mehhhhh..... boring, over complicated just do list comprehension & lambda supremacy


