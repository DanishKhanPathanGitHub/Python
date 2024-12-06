#help(float)
from fractions import Fraction

print(float(10))
print(float(0.1))
print(format(0.1, '.15f'))
print(format(0.1, '.20f'))
print(format(0.125, '.35f'))
'''
Here floating point representation will be like >
ab.cd = a*2^1 + b*2^0 + c*2^-1 + c*2^-2
2^-1 = 1/2 fraction = which have exact value with precision = 0.5
2^-2 = 1/4 also have exact value with precsion = 0.25,
and same for 2^-3 = 1/8 = 0.125 
that's why we get exact representation of 0.125 in floats with any long precision
As, 0.125+0.25=0.375 also have exact float representation in binary/memory
'''
print(format(0.375, '.35f'))
'''
but as for floatings points which do not have exact binary representation will not
have exact representation of that floating value, 0.1 for instance, in memory
same for any float value which we can't get combination in binary to represent
ex. 0.3
'''
print(format(0.3, '.25f'))
print(Fraction(0.3))
x = 0.1+0.1+0.1
y = 0.3
print(f'x={format(x, '.20f')}, y={format(y, '.20f')}')
print(x==y) #off course it won't be same as reason we discussed above
print(round(x,15)==round(y,15)) #that's a one way for equality check of floats
#ROUND WILL compare values on absolute termms not relativly
#ex. 10000.01 can be = 10000.02 in absoulte and relative terms 
#but 0.01 can not be = 0.02 in relative terms but in absolute terms they can be
x, y = 10000.01, 10000.02
a, b = 0.01, 0.02
import math
print(math.isclose(x,y, abs_tol=0.001, rel_tol=0.01))
#comparitivly x and y is close..........checks rel_tol for larger numbers
print(math.isclose(a,b, abs_tol=0.01, rel_tol=0.01))
#but a and b is not close relativly to x and y.....checks abs_tol for smaller numbers

 