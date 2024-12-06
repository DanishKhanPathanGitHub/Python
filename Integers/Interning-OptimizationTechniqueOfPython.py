a = 10
b = a
#this will create object of int 10 in memory, a refencing to it
#then b will also refence to that 10 which is referenced by a, that's shared preference
A=10
B=10
Str1 = 'hello'
Str2 = 'hello'
'''for the immutable types, here string and integers, if two variables have same value
python will automatically refernce them to shared object in memory
because this is safe, changing that shared refernce object in memory is not possible
, and if you do so, that will create a new object in memory and won't affect that original shared object'''
print(f'Adress, of A is {id(A)}, and of B is {id(B)}')
print(f'Adress, of Str1 is {id(Str1)}, and of Str2 is {id(Str2)}')
list1 = [1,2,3]
list2 = [1,2,3]
print(f'Adress, of list1 is {id(list1)}, and of list2 is {id(list2)}')
'''But for the case of mutable object types, change in one object will affect the other
it will not refernce to the same object in memory for same values
Both variables have their own objects created in different memory address'''

'''python won't refernce a and b to same object int 290 in memory
rather it will create 2 different objects, because this shared preference for immutable data type
is for optimization of memory and operations, for ex... == operator will check the data inside the object
and compare it, but having same object, equality can be checked by just memory address comparision
But for that python have singeletons objects, for which python will refernce variable to  that object instead of creating new ones
for integers it's [-5, 256]
for strings if string is like of variable name. but to make any object singeleton
we have ineterning method
'''
a=290
b=290
print(f'if id a is {id(a)}')
print(f'if id b is {id(b)}')
print('a==b is: ', a == b)
print('a is b is: ', a is b)

'''same memory address for even 290'''
