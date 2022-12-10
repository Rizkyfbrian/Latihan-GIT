class Node: 
  def __init__(self, value): 
    self.value = value
    self.next = None

class Queue:
  def __init__(self): 
    self.head = Node("head") 
    self.size = 0

  def isEmpty(self): 
    return self.size == 0

  def peek(self):
    if self.isEmpty(): 
      raise Exception("Peeking dari antrian kosong")
    n = self.head
    while(n.next!=None):
      n=n.next
    return n.value

  def enqueue(self, value): 
    node = Node(value)
    n = self.head
    while(n.next!=None):
      n=n.next
    n.next = node
    self.size += 1

  def dequeue(self): 
    if self.isEmpty(): 
      raise Exception("dequeue dari antrian kosong")
    remove = self.head.next 
    self.head.next = self.head.next.next 
    self.size -= 1 
    return remove.value

  def getSize(self): 
    return self.size
#main Program
antri = Queue()
print("Ukuran antrian saat ini adalah",antri.getSize())
antri.enqueue('U')
antri.enqueue('N')
antri.enqueue('M')
antri.enqueue('O')
antri.enqueue('K')
antri.enqueue('E')
print("Ukuran antrian saat ini adalah",antri.getSize())
print("urutan data pertama saat ini",antri.dequeue())
print("urutan data pertama saat ini",antri.dequeue())
print("urutan data terakhir saat ini",antri.peek())
print("Ukuran antrian saat ini adalah",antri.getSize())
