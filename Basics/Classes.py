class rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
    def __repr__(self):
        return f'Reactangle ({self.width} x {self.height})'
    
    def __str__(self):
        return f'Reactangle ({self.width} x {self.height})'
    
    def __eq__(self, other):
        try:
            return self.width == other.width and self.height == other.height
        except:
            return False
         
r1 = rectangle(10,20)
r2 = rectangle(10,20)
r3 = rectangle(5,25)

print(f'representation of rectangle: {r1}')
print(r1==r2)
print(r1 is not r2)
print(r1==r3)
print(r1==4)