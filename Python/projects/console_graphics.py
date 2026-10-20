# import time
# start = time.perf_counter()

from pynput import keyboard
from pynput.keyboard import Key

class pixel:
  def __init__(self,x:int,y:int,z:int):
    self.x = x
    self.y = y
    self.z = z 
    self.distance = 0
  
  def __str__(self):
    return f"{self.x} {self.y} {self.z}"

class xyzclass:
  def __init__(self,x:int,y:int,z:int):
    self.x = x
    self.y = y
    self.z = z 

def view(a: list, pixels: list, xyz: xyzclass):
  apply_pixels(a, pixels, xyz)
  for i in reversed(range(len(a))):
    for j in range(len(a[i])):
      print(a[i][j]*2, end="")
    print("")

def apply_pixels(a: list, pixels: list, xyz: xyzclass):
  symbols = ["█", "▓", "▒", "░", "≡", "=", "-", "."]
  Symblos_len = len(symbols) -1

  if xyz.x == 0 and xyz.y == 0 and xyz.z == 1: # будем просто изменять список пикселей а отрисовку оставим одну всегда, но это уже завтра
    for pix in pixels:
      if pix.z > Symblos_len:
        pix.z = Symblos_len
      dis = 0
      for sym in symbols:
        if a[pix.y][pix.x] == sym:
          dis = 1
          if symbols.index(sym) > pix.z:
            a[pix.y][pix.x] = symbols[pix.z]
      if dis == 0:
        a[pix.y][pix.x] = symbols[pix.z]

def create(lines: int, columns: int):
  a = []
  for _ in range(lines):
    line = []
    for _ in range(columns):
      line += [" "]
    a += [line] # or a.append(line)
  return a

def cybe(size: int):
  a = []
  for x in range(size):
    for y in range(size):
      b = pixel(x,y,0)
      a += [b]
  return a

def line(size: int):
  a = []
  for i in range(size):
    a += [pixel(i,i,i)]
  return a

def on_press(key):
    global zone, pixels, xyz
    print(": ", end="")
    if key == Key.up:
      xyz.y = 1
      xyz.x = 0
      xyz.z = 0
      view(zone,pixels,xyz)
    elif key == Key.down:
      print("!!")
    elif key == Key.left:
      print("!!")
    elif key == Key.right:
      print("!!")
    elif key == Key.esc:
      return False
    else:
      return 
if __name__ == "__main__":
  pixels = cybe(4) # cybe or line
  zone = create(15,15)
  xyz = xyzclass(0,0,1)
  view(zone,pixels,xyz)
  with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



# end = time.perf_counter()
# print(f"выполнилось за: {end - start:.6} секунд")

# pixels = []
# pixels += [pix1 := pixel(0,0,2)]

# for el in pixels:
#   print(el)