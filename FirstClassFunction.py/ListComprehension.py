print(list(map(lambda x: x**2, [1,2,3,4])))
#map function takes a function, and iterable, 
#passes the iterable elements as arguments to function and return new iterable object
#here, lambda function - x parameter
# list as parameter to map, each element of list 
# will be passed as parameter x to lambda  
List = [1,2,3,4]
List_even = list(filter(lambda x: x%2 == 0, [1,2,3,4]))
print(f'List = {List}')
print(f'List_even = {List_even}')
#takes function, takes iterable
#each element of iterable will be passed as arg to funct
#for that element if func returns false then element will be removed else kept
#returns a new list, org won't be changed

l1 = [1,2,3,4]
l2 = 'python'
print(list(zip(l1, l2)))
#Zip will bound the respective elements of 2 iterables and makes tuples of it
#result will of the length of smallest size of iterable, 

#List comprehesnion
l1, l2 = [1,2,3,4,5], [10,20,30,40,50]
#map way:
print(list(map(lambda x, y: x+y, l1,l2)))
print(list(map(lambda x: x**2, l1)))
#List comprehension way:
print([x**2 for x in l2])
print([x+y for x, y in zip(l1, l2)])

#filter alternative List comprehension:
List = [1,2,3,4]
List_even = [x for x in List if x%2==0]
print(List_even)
#List comprehension SUPREMACY!!!
