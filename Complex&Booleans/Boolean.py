print(type(True))
print(int(True))
print(True==1, True is 1)
a = True
b = False
print(id(a), id(b))
print(bool(2+3==3))
print(issubclass(bool, int))
#boolean is sub class of int clss. boolean values False=0, everything else is True
#but int(True) = 1, and True and False are singleton objects 
# means memory address of them will remain same for the lifetime of code
print(10+(True*100))

#precedence of operators
#<, >, <=, >=, ==, != in is
#not
#and
#or
x = 1<2>0
x1 = 1<2 and 2>0 #that's how above statement executed
print(x)
print(x==x1)

print('a' or [1,2])
print('a' and [1,2])
print('' or [1,2])
print('a' and [])
#for or operator see it's first value, if it's true it doesn't even look value after or
#and returns it, if it's false, returns value after or, for and exactly opposite
#for and operators, it sees, first value, if it's true, returns second value
#if it's false, returns it, & it doesn't look for value after and


