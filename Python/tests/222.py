import sys
import animals
from animals import Humanoid as Hum


print(sys.modules['__main__'])
my_cat = animals.Animal("cat", 7)
zombie = Hum('Monster', 333)

print(zombie.age)
print(my_cat.age)
