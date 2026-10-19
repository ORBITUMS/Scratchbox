def f():
    yield 1
    print("hi")
    yield 2
    print(67)
    yield 3

while True:
    a = 1
    g = f()
    while a == 1:
        a = int(input("input: "))
        try:
          next(g)
        except:
            print("hah")
            print(str(f()))
            print(str(f()))
            print(str(f()))
            print(str(f()))
