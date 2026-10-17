class Element:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self.lenght = 0
    self.first = None
    self.last = None
  
  def add(self, value):
    a = Element(value)

    if self.first == None:
      self.first = a
      self.last = a
      self.lenght = 1
    else:
      self.last.next = a
      self.last = a
      self.lenght += 1

  def debug(self):
    a = self.first
    i = 1
    while a != self.last:
      print(f' значение {i}: {a.value}, next = {a.next}')
      i += 1
      a = a.next
    print(f' значение {i}: {a.value}, next = {a.next}')
    print(f'всего элементов: {self.lenght}')



if __name__ == '__main__':
  el1 = Element(52, 1)
  print(el1.__dict__)