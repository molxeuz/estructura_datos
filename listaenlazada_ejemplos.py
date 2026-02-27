class Node:

  __slots__ = ('__value','__next')

  def __init__(self,value):

    self.__value = value
    self.__next = None

  @property
  def value(self):
    return self.__value

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self, new_next):
    if new_next is not None and not isinstance(new_next,Node):
      raise TypeError("El next solo pueder ser un objeto Node ó None.")
    self.__next = new_next

  @value.setter
  def value(self, new_value):
    if new_value is None:
      raise ValueError("El valor del nodo no puede ser null ó None.")
    self.__value = new_value


  def __str__(self):
    return str(self.__value)

#node1 = Node(10)
#node2 = Node(20)
#node1.next = node2
#node2.next = 89

#print(node1)
#print(node2)

class LinkedList:

  __slots__ = ('__head','__tail','__size')
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  def __iter__(self):
    current_node = self.__head
    while current_node is not None:
      yield current_node
      current_node = current_node.next

  def __str__(self):

    result = [str(node) for node in self]
    return ' --> '.join(result)

  def prepend(self, new_value):
    new_node = Node(new_value)

    if self.__head is None:
      self.__head = new_node
      self.__tail = new_node
    else:
      new_node.next = self.__head
      self.__head = new_node

    self.__size += 1

  def append(self, new_value):
      new_node = Node(new_value)

      if self.__head is None:
        self.__head = new_node
        self.__tail = new_node
      else:
        self.__tail.next = new_node
        self.__tail = new_node

      self.__size += 1


  def get_by_index(self, index):

    if index < -1 or index > self.__size -1:
      raise ValueError("indice fuera de rango.")

    if index == -1:
      return self.__tail

    current_index = 0
    for current_node in self:
      if index == current_index:
        return current_node
      current_index += 1



    #current_node = self.__head
    #for _ in range(index)
    #  current_node = current_node.next

    # return current_node

  def insert_by_index(self, index, new_value):

    if index < -1 or index > self.__size:
      raise ValueError("indice fuera de rango.")

    if index == 0:
      self.prepend(new_value)
    elif index == -1 or index == self.__size:
      self.append(new_value)
    else:
      new_node = Node(new_value)
      prev_node = self.get_by_index(index-1)
      new_node.next = prev_node.next
      prev_node.next = new_node
      self.__size += 1

  def search_value(self,value):

    for current_node in self:
      if current_node.value == value:
        return True

    return False


  def set_new_value(self, value, new_value):
    for current_node in self:
      if current_node.value == value:
        current_node.value = new_value
        return True

    return False

  def pop_first(self):

    if self.__head is None:
      print("Lista vacia!!")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__head
      self.__head = self.__head.next
      self.__size -= 1
      popped_node.next = None
      return popped_node

  def pop(self):

    if self.__head is None:
      print("Lista vacia!!")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__tail
      prev_tail = self.get_by_index(self.__size-2)
      print("prev_tail",prev_tail)
      self.__tail = prev_tail
      self.__tail.next = None
      self.__size -= 1
      return popped_node

customLL = LinkedList()
customLL.prepend(50)
print("lista despues del primer prepend: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)
customLL.prepend(70)
print("lista despues del 2do prepend: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)
customLL.append(40)
print("lista despues del 1er append: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)

customLL.append(80)
print("lista despues del 2do append: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)

customLL.prepend(30)
print("lista despues prepend: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)
print("customLL.size",customLL.size)

print("nodo en la posicion 2",customLL.get_by_index(2))
print("nodo en la posicion 4",customLL.get_by_index(4))

print("nodo nuevo 120 en la posicion 2")
customLL.insert_by_index(2,120)
print("lista despues insert_by_index: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)
print("customLL.size",customLL.size)

print("nodo nuevo 150 en la posicion = size")
customLL.insert_by_index(6,150)
print("lista despues 2do insert_by_index: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)
print("customLL.size",customLL.size)

print("busqueda del valor 50 :",customLL.search_value(50))
print("busqueda del valor 1 :",customLL.search_value(1))

print("cambiar el valor 120 por 5 :",customLL.set_new_value(120,5))
print("lista despues set_new_value: ",customLL)

print("llamado metodo pop_first : ")
nodo_eliminado = customLL.pop_first()
print("nodo_eliminado",nodo_eliminado)
print("lista pop_first: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)
print("customLL.size",customLL.size)

customLL2 = LinkedList()
print("llamado metodo pop_first lista vacia : ", customLL2.pop_first())
print("lista pop_first: ",customLL2)
print("customLL.head",customLL2.head)
print("customLL.tail",customLL2.tail)
print("customLL.size",customLL2.size)
customLL3 = LinkedList()
customLL3.append(7)
print("llamado metodo pop_first, lista 1 solo nodo : ")
nodo_eliminado = customLL3.pop_first()
print("nodo_eliminado",nodo_eliminado)
print("lista pop_first: ",customLL3)
print("customLL.head",customLL3.head)
print("customLL.tail",customLL3.tail)
print("customLL.size",customLL3.size)

print("llamado metodo pop : ")
nodo_eliminado = customLL.pop()
print("nodo_eliminado",nodo_eliminado)
print("lista pop_first: ",customLL)
print("customLL.head",customLL.head)
print("customLL.tail",customLL.tail)
print("customLL.size",customLL.size)
