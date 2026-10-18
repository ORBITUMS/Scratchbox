import time
start = time.perf_counter()

class pixel:
  def __init__(self,x:int,y:int,z:int):
    self.x = x
    self.y = y
    self.z = z 
    self.distance = 0
  
  def __str__(self):
    return f"{self.x} {self.y} {self.z}"


def view(a: list, pixels: list, xyz: str):
  apply_pixels(a, pixels, xyz)
  for i in reversed(range(len(a))):
    for j in range(len(a[i])):
      print(a[i][j], end="")
    print("")

      
def create(lines: int, columns: int):
  a = []
  for _ in range(lines):
    line = []
    for _ in range(columns):
      line += [" "]
    a += [line] # or a.append(line)
  return a

def apply_pixels(a: list, pixels: list, xyz: str):
  symbols = ["█", "▒", "░","."]
  if xyz == "z":
    for pix in pixels:
      if pix.z > 3:
        pix.z = 3
      dis = 0
      for sym in symbols:
        if a[pix.y][pix.x] == sym:
          dis = 1
          if symbols.index(sym) > pix.z:
            a[pix.y][pix.x] = symbols[pix.z]
      if dis == 0:
        a[pix.y][pix.x] = symbols[pix.z]
  elif xyz == "x":
    for pix in pixels:
      if pix.x > 3:
        pix.x = 3
      dis = 0
      for sym in symbols:
        if a[pix.y][pix.z] == sym:
          dis = 1
          if symbols.index(sym) > pix.x:
            a[pix.y][pix.z] = symbols[pix.x]
      if dis == 0:
        a[pix.y][pix.z] = symbols[pix.x]


  return a

def cybe(size: int):
  a = []
  for x in range(size):
    for y in range(size):
      b = pixel(x,y,0)
      a += [b]
  return a

if __name__ == "__main__":
  zone = create(10,10)

  pixels = cybe(6)
  # pixels = []
  # pixels += [pix1 := pixel(0,0,2)]
  
  view(zone,pixels,"z")
  # for el in pixels:
  #   print(el)

end = time.perf_counter()
print(f"выполнилось за: {end - start:.6} секунд")