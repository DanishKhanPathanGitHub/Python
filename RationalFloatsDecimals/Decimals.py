from decimal import Decimal
import decimal
x = Decimal(1.25)
y = Decimal(1.35)
#Decimal constructor can have integer, tuple and float data type as parameters
#float value will be actually represented as in 52 digits after decimal point
#which is how float exactly stored in memory
print('x: ', x)
print('y: ', y)
#that's why we use tuples and strings to represent the decimals
print(Decimal('1.35'))
print(Decimal((1, (1,3,5), -2)))
#(sign (digits), n) sign*digits x 10^-n, 0:positive, 1:negative
#here sign:1:negative, digits: 1,3,5, n=-2  -135 x 10^-2
print('rounding of x: ', round(x, 1))
print('rounding of y: ', round(y, 1))
print('global context: ', decimal.getcontext(), 'rounding type: ', decimal.getcontext().rounding)
print('local context: ', decimal.localcontext())
#here this local context will be of context manager type
#getcontext would be context type
#we can use another rounding algorithms also by setting rounding type 
#but changing that will affect globally, so we should do it localy
with decimal.localcontext() as lctx:
    lctx.prec = 6
    lctx.rounding = decimal.ROUND_HALF_UP
    print('rounding of x in ROUND_HALF_UP: ', round(x, 1))
    print('rounding of y: ROUND_HALF_UP', round(y, 1))
    print(decimal.getcontext() == lctx)

#here within perticular scope, getcontext and loclcontext would be same
#Now what is this prec = precision means? 
#It does not mean that while creating decimals, 
# we limit the digits after the decimal point to that prec
# It will not affect constructor, but the output of mathematical computations
#Ex below:

with decimal.localcontext() as lctx:
    a = Decimal('1.234567')
    b = Decimal('1.234567')
    lctx.prec = 4
    print(f'a={a}, b={b}')
    print(f'a+b={a+b}')
    lctx.prec=28
    print(f'a+b={a+b}')
    print(decimal.getcontext() == lctx)
#1.234567 won't be rounded to prec(here 4) but when any mathematical operation made on..
#It will be rounded up to that prec(here, 4) deigits
x = Decimal(-10)
y = Decimal(3)
x1 = float(-10)
y1 = float(3)
print(f'x//y = {x//y}, x%y = {x%y}')
print(f'x1//y1 = {x1//y1}, x1%y1 = {x1%y1}')
#x//y for integers & floats do floor division, returns max num<=result,i.e.for -3.1, -4
# but for decimals  it will do truncation division,i.e. for -3.1, -3
a = Decimal('1.5')
print(a.ln())
print(a.exp())
print(a.sqrt())
#For decimals it takes more memory than floats. performance is also slower
import sys
import math
a = 33.125333333333333333333
a_dec = Decimal('33.125333333333333333333')
print(sys.getsizeof(a))
print(sys.getsizeof(a_dec))

import time

def run_float(n):
    for i in range(n):
        a = 1.2345
        math.sqrt(a)

def run_decimal(n):
    for i in range(n):
        b =Decimal('1.2345')
        b.sqrt()

start = time.perf_counter()
run_float(10000)
end = time.perf_counter()
print('for float time: ', end-start)

start = time.perf_counter()
run_decimal(10000)
end = time.perf_counter()
print('for Decimal time: ', end-start)

#With priciseness and accuracy, Decimals compromises the time -wisdom
