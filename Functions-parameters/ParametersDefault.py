from datetime import datetime
import time
print(datetime.now())

def log(msg, *, dt=datetime.now()):
    print(f'{msg} at {dt}')

log("messga-1", dt="2001-01-01 00:00:00.000")
log("messga-2")
time.sleep(5)
log("message-3")
nums = [1,2]
def func(a, b, nums=nums):
    print(f'a={a}, b={b}, c={sum(nums)}')

a,b=2,3
nums = [a,b]
func(a, b, nums)
func(a,b)
    
#notice when we run log after 10 sec again, dt will be same
#because dt if not provided, give default value
#default value don't executed on fucntion call
#default value of any parameter get evaluated at the function definition
#so here datetime won't be get new value every time we run but will have default value
#which is assigned at func def 

def log(msg, *, dt=None):
    dt = dt or datetime.now()
    print(f'{msg} at {dt}')


log("messga-4")
time.sleep(5)
log("message-5")

#that's one way we can handle setting parameter default value at runtime 
# by setting them to None and then give default value at runtime if not provided

#we should not use mutable data type as parameters 
# and should approach in above way