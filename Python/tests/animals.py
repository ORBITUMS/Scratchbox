class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
    print(self) 

class Humanoid:
  def __init__(self,name,age):
    self.name = name
    self.age = age



if __name__ == '__main__':
  print(type(__name__))
  __name__ = "main"
  print(__name__)
  my_dog = Animal('Джек', 6)
  print(my_dog.name) 
  print(my_dog.age)
