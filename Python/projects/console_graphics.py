# import time
# start = time.perf_counter()

# сделать потом вращяющяюся шнягу какую-нибудь
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

# class xyzclass:
#   def __init__(self,x:int,y:int,z:int):
#     self.x = x
#     self.y = y
#     self.z = z 

def view(pixels: list): # xyz: xyzclass
  Frame = apply_pixels(pixels)
  for i in reversed(range(len(Frame))):
    for j in range(len(Frame[i])):
      print(Frame[i][j]*2, end="")
    print("")

def apply_pixels(pixels: list): # xyz: xyzclass
  a = create(15,15)
  symbols = ["█", "▓", "▒", "░", "≡", "=", "-", "."]
  Symbols_len = len(symbols)-1
  for pix in pixels:
    z = pix.z
    if z > Symbols_len:
      z = Symbols_len
    
    try:
      a[pix.y][pix.x] = symbols[z]
    except:
      pass
  return a

def create(lines: int, columns: int):
  a = []
  for _ in range(lines):
    line = []
    for _ in range(columns):
      line += [" "] # " "
    a += [line] # or a.append(line)
  return a

def cybe(size: int):
  pixels = []
  for x in range(size):
    for y in range(size):
      px = pixel(x,y,0)
      pixels += [px]
  return pixels

def line(size: int):
  a = []
  for i in range(size):
    a += [pixel(i,i,i)]
  return a

def on_press(key):
    global pixels
    if key == Key.up:
      for px in pixels:
        px.y += 1
      view(pixels)
    elif key == Key.down:
      for px in pixels:
        px.y -= 1
      view(pixels)
    elif key == Key.left:
      for px in pixels:
        px.x -= 1
      view(pixels)
    elif key == Key.right:
      for px in pixels:
        px.x += 1
      view(pixels)
    elif key == Key.shift_r:
      for px in pixels:
        px.z += 1
      view(pixels)
    elif key == Key.shift_l:
      for px in pixels:
        px.z -= 1
      view(pixels)
    elif key == Key.esc:
      return False
    elif key == Key.alt_r:
      for px in pixels:
        x = px.x
        px.x = px.z
        px.z = x
      view(pixels)
    elif key == Key.alt_l:
      for px in pixels:
        x = px.x
        px.x = px.y
        px.y = x
      view(pixels)
    else:
      return 

if __name__ == "__main__":
  pixels = cybe(7) # cybe or line
  # xyz = xyzclass(0,0,1)
  view(pixels) #xyz
  with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



# end = time.perf_counter()
# print(f"выполнилось за: {end - start:.6} секунд")

# pixels = []
# pixels += [pix1 := pixel(0,0,2)]

# for el in pixels:
#   print(el)