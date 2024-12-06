#variable as memory references
a = 10
b = 10
c = a
print(f'id of a: {id(a)}, id of b: {id(b)}, id of c: {id(c)}, id of 10: {id(10)}' )
print(a==b)
print(c==10)

#refernce counting:
import sys
list_a = [1,2,3]

print(f'reference count of list_a: {sys.getrefcount(list_a)}')
#this funnction will actually return count of variables referencing the object in memory + 1
print(f'reference count of b: {sys.getrefcount(b)}')

list_b = list_a
print(f'reference count of list_b: {sys.getrefcount(list_b)}')

import ctypes

def get_reference(address):
    return ctypes.c_long.from_address(address).value 
    #this thing will get exact count of variables referencing to the object at the given address in memory

print('reference count of list_b: ', get_reference(id(list_b)))

list_a = [1,2]
print('reference count of list_a: ', get_reference(id(list_a)))
print('reference count of list_b: ', get_reference(id(list_b)))

#refernce counting: python memory management will destroy the object 
#as soon as reference count to that memory address of object will be 0
id_of_list_a = id(list_a)
list_a = None #now list_a object referencing to the memory address, that will be free
#and refernce count to that memory object will be 0 and will be made available for others
print('reference count of object at memory address of id_of_list_a: ', get_reference(id_of_list_a))#that will be zero
print('reference count of list_a: ', get_reference(id(list_a)))

