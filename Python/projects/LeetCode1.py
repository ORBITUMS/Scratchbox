import sys

print = sys.stdout.write
#data = list(map(int, sys.stdin.readline().split()))
data = int(sys.stdin.readline())

ans = []

def f(l: int, r:int,st:str):
    global ans
    #0
    if r == 1 and l == 0:
       ans += [st+")"]
       return None
       
    #1
    if l > 0:
        f(l-1,r,st+"(")
    #2
    if r > l: #!!!!!!
        f(l,r-1,st+")")


if data > 0:
    f(data , data, "")
print(str(ans))
