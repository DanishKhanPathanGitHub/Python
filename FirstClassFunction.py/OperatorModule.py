import operator
from functools import reduce
print(operator.mul(3,4))

Product = lambda x, y: x*y
print(reduce(Product, [3,4,5]))

#hey, hold my cock you lambda, i don't need you, operator is my new friend
print(reduce(operator.mul, [3,4,5]))
print(TypeError(operator.mul))
#there are many other function methods in operator class
#print(help(operator))
print(operator.getitem([1,2,3], 1))  #different code techniques gymnastics
print(operator.itemgetter('c')({'a':1, 'b':2, 'c':3}))  

List = [1+ 2j, -4+-9j, 10j, 11+-1j ]
print(sorted(List, key=lambda x: x.real)) 
#let's do some gymnastics to make things complex diliberately...LOL
print(sorted(List, key=operator.attrgetter('real'))) 
#here attrgeter will basically apply the method on each object of List
#and get's the .real value of object
