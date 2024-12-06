import sys
print(sys.getsizeof(2)) #160 bytes (160)*8 = bits
import math

print('<----floor, division of positive int--->')
print(10/3) #float
print(10//3) #will floor same as below
print(math.floor(10/3)) #which returns largest number <= (10/3=3.33)
print(math.trunc(10/3)) 

print('<----floor, division of negative int--->')
print(-10/3)
print(-10//3) #here -3.33, largest number <= -3.33 will be -4 here
print(math.floor(-10/3))
print(math.trunc(-10/3)) #here truncate will just trunc 0.333 so -3
print(6/-132)
print(6//-132) 
print(math.floor(6/-132))
print(math.trunc(6/-132)) #here truncate will just trunc 0.333 so -3
print('<----division modular and floor formula--->')
a=10
b=-3
print(a == b*(a//b) + (a%b))

print("<---!-------------------->")

print((1.2))