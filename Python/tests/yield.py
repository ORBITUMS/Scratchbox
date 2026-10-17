
def counter(n):
  print("start")
  for i in range(n):
        print(f"перед yield {i}")
        yield i ## yield i
        print(f"после yield {i}")



if __name__ == "__main__":
  print("version 1.x.x")
  gen = counter(3)
  print(gen)
  print(next(gen))
  print(next(gen))
  print(next(gen))
  print(next(gen))
