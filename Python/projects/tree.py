def pyramid(n):
    i = 1
    while n > 0:
        n -= 1
        yield " "*n + "*"*i   # <-- вот здесь магия
        i += 2



num = int(input("input number of rows: ")) 

for row in pyramid(num):
    print(row)