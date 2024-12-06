import time

def timerfunc(fun, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fun(*args, **kwargs)
    end = time.perf_counter()
    return end-start

print_time = timerfunc(print, "hello world", "how are you?", sep='**', end="\n\n", rep=1000)
print(print_time)