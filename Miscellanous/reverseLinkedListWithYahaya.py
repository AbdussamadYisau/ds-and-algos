class Node:
  def __init__(self,data = None):
    self.data = data
    self.next = None
    
class linkedList:
  def __init__(self):
    self.head = Node()
#  def append(self,data):
#   temp = Node(data)
  # if self.head is None:
    # self.head = temp
      #return
    #p = self.head
    #while p.next is not None:
    # p = p.next
    #p.next = temp  
  def append(self ,value):
    if self.head.data == None:
      self.head = Node(value)
      return
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      temp.next = Node(value)
    
  def display(self):
    a = []
    temp = self.head
    while temp != None:
      a.append(temp.data)
      temp = temp.next
    print(a)
    
  def reverse(self):
    prev = None
    present = self.head 
    while present != None :
      next = present.next
      present.next = prev 
      prev = present
      present = next
    self.head = prev
    
      
      
mylist = linkedList()
mylist.append(3)
mylist.append(42)
mylist.append(34)
mylist.append(35)
mylist.append(0)
mylist.append(5)
mylist.display()
mylist.reverse()
mylist.display()





# https://www.geeksforgeeks.org/reverse-a-linked-list/
