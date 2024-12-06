#See unpackingIterables first before this code
def sum(num1, num2, *args):
    sum = num1+num2
    print(args)
    for n in args:
        sum+=n
    return sum

#args will unpack all parameters passed on fuction into a tuple
#same way we were unpacking iterables and assigning to a variable, here arg
print(sum(1,2,3,4)) #num1=2, num2=2, args=(3,4)
print(sum(4,5)) #num1=2, num2=2, args=()
#args are basically optional parameters
