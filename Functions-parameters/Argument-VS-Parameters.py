def sum(a1, a2=0, a3=0):
    return a1+a2+a3
#once we define keyword argument, it must not be any positional arguments after it.
#here ex. sum(a1, a2=0, a3) not allowed, fpr both arguments and parameters
#argument: while calling func, parameter: while defining func
print(sum(a2=10, a1=2))

