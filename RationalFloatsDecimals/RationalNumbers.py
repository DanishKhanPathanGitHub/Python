from fractions import Fraction
import math

num = Fraction(6,10) #numerator, denominator
print(num)
print(num.denominator)
print(num.numerator)

x = Fraction(math.pi) #pi is irrational number but stored as float in memory
#which are having finite precision and real numbers
print(x)
pi2 = x.limit_denominator(100000)
print(pi2)
pi3 = x.limit_denominator(1000)
print(pi3)
pi4 = x.limit_denominator(10)
print(pi4)
#denominator precision control



