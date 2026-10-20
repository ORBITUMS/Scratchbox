import time

def f():
    while True:
        print(1)
        yield 1
        print(2)
        yield 2
        print(3)
        yield 3

time.sleep(0.1)
while True:
    a = 1
    g = f()
    while a == 1:
        next(g)
        time.sleep(0.5)

