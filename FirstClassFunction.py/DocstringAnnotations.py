
def Print(a, *b):
    "this func will print a and optinal b will rerurn nothing"
    print(a)
    for c in b:
        print(b)

#Firts string of the function body will be stored as docstring for function
help(Print)

def sumOfList(nums: list[int], n: int) -> int :
    "will sum the first n number of nums list"
    return sum(nums[:n])

help(sumOfList)
print(sumOfList.__annotations__)
print(sumOfList.__doc__)
