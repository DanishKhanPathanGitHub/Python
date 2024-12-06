a = 10
print(f'id of a: {id(a)}')
a = 12
print(f'id of a after change: {id(a)}')
list_a = [1,2,3]
print(f'id of list_a: {id(list_a)}')
list_a.append(4)
print(f'id of list_a after change: {id(list_a)}')

#immutable objects won't allow to change internal data of an object at perticular memory address
#when you change the data it's actually new object created at different address
tuple_a = (1,2,3)
#tupple by default don't have mutable functions like append, add, delete etc..
#numeric types, Strings, tuples, are immutable objects
#sets, dictionaries, lists are mutable objects
tuple_of_list = ([1], [3,4])
print(f'id of tuple_of_list: {id(tuple_of_list)}')
print(f'id of tuple_of_list[0]: {id(tuple_of_list[0])}') #1.a
print(f'id of tuple_of_list[1]: {id(tuple_of_list[1])}') 
tuple_of_list[0].append(2)
print(f'id of tuple_of_list after change: {id(tuple_of_list)}')
print(f'id of tuple_of_list[0] aftrer change: {id(tuple_of_list[0])}') #1.b
'''if individual object of immutable objects, are mutable then they are mutable itself
and it won't affect the mutability of immutable object, 
as memory address of it's individual object is not affected by it. see how 1.a and 1.b are same
it's just internal data of object inside the mutable object which is inside the immutable object, is changing
which is because of mutability of that perticular object inside the immutable object, 
not related to immutable object itself'''
