class pixel:
  def __init__(self,x:int,y:int,z:int, symbol:str):
    self.x = x
    self.y = y
    self.z = z 
    self.sym = symbol
    self.distance = 0
  
  def me(self):
    print(f"{self.x} {self.y} {self.z}") 


def view(a: list):
  for i in reversed(range(len(a))):
    for j in range(len(a[i])):
      print(a[i][j], end="")
    print("")
      
def create(lines: int, columns: int):
  a = []
  for _ in range(lines):
    line = []
    for _ in range(columns):
      line += ["."]
    a += [line] # or a.append(line)
  return a

def apply_pixel(a: list, pix: pixel):
  a[pix.x][pix.y] = pix.sym
  return a


if __name__ == "__main__":
  pix1 = pixel(0,0,4, "!") #pixel(1,3,4, "!")
  pix1.me()

  zone = create(4,20)

  apply_pixel(zone,pix1)
  
  view(zone)

# TODO: use z as distance; keep a list of symbols per distance.