
sumlambda =  lambda x, y=0: x+y
print(sumlambda(1,4))
print(type(sumlambda))
#so lambda are function, which can be passed to another function
#because every function is first class function in python 
#first class function has below attributes
#they can be passed into another function, can be return from another function
def apply_func(fn, *args, **kwargs):
    print(fn(*args, **kwargs))

apply_func(lambda nums, n=-1: sum(nums[:n]),  [1,2,3,4,5,6])
nums = [1,2,3,4,5,6]
print(nums[:-1])

List = ['s', 'A', 'X', 'n', 'O', 'd']
print(sorted(List))
#Uppercase values have lower ascii code that's why X O will come before s,d,n
#we can do sorting based on the key value associated with each value of list
#sorted method hase key parameter, which is None by default'
#if we provide key for each value of the List,
#List will sorted  based on that key

print(sorted(List, key=lambda s: s.upper())) 
#that will associate uppercase char as key to each value of List
#aand now based on that key, List will be sorted
print(sorted(List, key=lambda s: List.index(s)) )
#above lline is basically won't sort anything, we associated index value
#so it will be same as index value will be used for sorting
#this is helpful for dictionaries which is sorted by default based on the keys
#we can sort dicts based on the values
dix = {'a':200, 'b':300, 'c':100}
print(sorted(dix))
print(sorted(dix, key=lambda x: dix[x]))
#here we are associating dix[x] which is value of key of dix, as key for sorting
 
#randomizing the list
import random
print(random.random)
List = [1,2,3,4,5,6,7]
print(sorted(List, key=lambda x: random.random()))