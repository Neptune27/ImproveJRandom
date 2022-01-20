import time


def wrapper(f):
    start = time.perf_counter_ns()
    f()
    print(time.perf_counter_ns() - start)


@wrapper
def add():
    a = []
    for i in range(1000):
        a.append(i)


@wrapper
def minus():
    a = []
    for i in range(1000):
        a.append(i)
