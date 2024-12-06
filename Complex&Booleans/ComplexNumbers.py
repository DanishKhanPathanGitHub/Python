a = 1+2j
b = complex(1,2)
print(f'a==b: {a==b}, real={a.real}, imaginary:{a.imag}' )
a=b+1
print(a)
print(a/2)
#so real and imag part of complex nums are stored as floats
#all of the operators except div & mod // and % will work same as per rules of floats 
#so prescision problem we had with floats will be same for complex numbers
p = 0.1 + 2j
print(format(p.real, '.25f'))
#math library also won't work, we have cmath lib for complx nums
import cmath
print('sqrt of 0.1+2j : ', cmath.sqrt(p))
print(abs(p))
print(cmath.sqrt(p.real**2 + p.imag**2))
#that's distancee between real and imag vectors of complx num
#x. for 1+1j, phase between this vectors is 45 degree, pi/4 (x=1, y=1)
#distance between these 2 vectors, sqrt(real^2+imag^2) 
#that we can handle automatically by abs() method as above
print('phase of 1+1j : ', cmath.phase(1+1j))
print(cmath.pi/4)
#rectangular reprs: point(complex num) reprs as cordinates of x & y
#polar reprs: diatance b|w imag and real, and phase b|w them ->
#we can get rect reprs from polar and polar from rect
#polar from rect by abs() for distance and cmath.phase() for phase
#rect from polar by cmath.rect(distance, phase)
print(cmath.rect(abs(p), cmath.phase(p)))
print(format(1.22222e-13j, '.19f'))
#as prescise problem with floats we used isclose for comparing values
#we use same method here also to deal with that problem of abs tol and rel tol
print(cmath.isclose(1.22222e-13j, 0, abs_tol=0.001))

