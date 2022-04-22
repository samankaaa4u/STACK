class Stack:
  def __init__(self, maxsize=0):
    self.collection = list()

    if maxsize < 0:             # If maxsize is negative value
      raise Exception('Cannot be negative.')

    self.maxsize = maxsize

  def size(self):
    return len(self.collection)

  def push(self, value):

    if self.size() < self.maxsize or self.maxsize == 0:
      self.collection.append(value)
    else:
      print('The stack is full')


  def pop(self,):
    if self.empty():
      print('The stack is empty')
      return
    print(f'{self.collection[-1]} is popped')
    self.collection.pop()


  def top(self):
    if self.empty():
      print('The stack is empty')

    print(self.collection[-1])

  def empty(self,):
    return self.size() <= 0

  def __str__(self):    # If we print the object, it will print the collection list
    return str(self.collection)


students = Stack(maxsize=5) # if no arguments then the stack is infinite
students.push('Sam')
students.push('Tom')
students.push('Mico')
students.push('Archie')
students.push('Janz')
students.push('Philip')
print(students)

for _ in range(7): # Pop 7 times
  students.pop()

students.push('Philip')
students.top()
students.push('Mico')
print(students.size())