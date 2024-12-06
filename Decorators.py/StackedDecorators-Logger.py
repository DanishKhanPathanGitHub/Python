def logged(fn):
    from functools import wraps
    from datetime import timezone, datetime

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{fn.__name__} called at: {run_dt}')
        return result
    return inner

@logged
def add(a, b):
    return a+b

#nothing, same code as we did prev, for timer
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

#Now we will use 2 decorators.
@logged #logged decorate the timer func 
@timer #timer decorate the mult
#excution of logged will be called, but inside timer will be called
#and inside that mult will be called. 
#mult 'll finish exc, after tht timer 'll finish exc, after tht logged 'll finsh exc
def mult(a, b):
    print(f'result of a x b: {a*b}')
    return a*b
#we can say upwards to downwards -> starting of execution
# downwards to upwards -> finishing execution
import time
add(8, 9)
time.sleep(3)
mult(4,6)
