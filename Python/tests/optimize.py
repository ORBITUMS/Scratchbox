import sys
# import time
input = sys.stdin.readline

people = int(input()) # count a people
it = 1
while people != 1:
  if people % 2 == 0:
    people = people//2
  else:
    people +=1
    people = people//2
  print(f"{it} {people}")
  it+=1
  # time.sleep(1/10)

print(f"количество итераций: {it-1}")