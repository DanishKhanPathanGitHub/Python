from functools import reduce
l = [5,8,6,10,9]
Max = lambda x, y: x if x>y else y
print(reduce(Max, l ))

#reduce function take a function and a iterable which can be indexed
#as parameter and based on the function give output
#here lambda function applied on l, which is to find maximum
#here, x would be at first index and y at 2nd, function will move
#y and compare to existing x(which is result, here max) 
#and replace acc to conditions
#5,8 5>8(else y), so 8; 8,6 8>6(x if x>y), so 8; 8,10 8>10 so 10; 10,9 10>9, so 10.
#this is how max(), min() or sum() like functions defined as below we discussed
Max = lambda x, y: x if x>y else y
def _max(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = Max(result, x)
    return result

Min = lambda x, y: x if x<y else y
def _min(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = Min(result, x)
    return result
Add = lambda x, y: x + y
def _add(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = Add(result, x)
    return result
#see the pattern, same pattern. we just neeed to change the function 
#generalize form:
def _reduce(sequence, fn):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

#Now we can call reduce to do many things like min, max or others on iterables
print(_reduce(fn=Add,sequence=[3,4,5] ))
Product = lambda x, y: x*y
print(_reduce(fn=Product,sequence=[3,4,5] ))
