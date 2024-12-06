
def timer(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        total = 0
        for i in range(10):
            start = perf_counter()
            fn_result = fn(*args, **kwargs)
            end = perf_counter()
            total+=(end-start)
        avg = total/10
        print(f'{fn.__name__} took {round(avg, ndigits=9)} time to complete')
        return fn_result
    return inner

def fibRecursive(n):
    """
    returns nth number of fibonacci series
    """
    if n <= 2:
        return 1
    return fibRecursive(n-2) + fibRecursive(n-1) 
  
@timer
def fib_recursive(n):
    return fibRecursive(n)
#reason we decorated this func which run and return actual fibRec func
#is that recursion function will run many times and will print thaat many times
#we just want to print the complete time taken by fibRec func, 
#not time of inside func calls. that's why nothing more  
print(fib_recursive(25))

@timer
def fibIterative(n:int)->int:
    """
    Prints fibonacci series untill nth number
    Returns nth number of fibonacci series
    """
    fibs = [1,1]
    if n <= 2:
        return fibs[n-1]
    for i in range(3, n+1):
        fibs.append(fibs[i-3]+fibs[i-2])
    print(fibs)
    return fibs[n-1]

print(fibIterative(25))



