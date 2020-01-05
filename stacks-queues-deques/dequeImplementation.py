class Deque(object):
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return (self.items == [])
	def addFront(self,item):
		return(self.items.insert(0,item))
	def addRear(self,item):
		return(self.items.append(item))
	def removeFront(self):
		return(self.items.pop(0))
	def removeRear(self):
		return(self.items.pop())
	def size(self):
		return(len(self.items))


d = Deque()

d.addFront("hello")

d.addRear("world")

print("The current size of the Deque: ",d.size())

print( d.removeFront() + " " + d.removeRear())

print("The current size of the Deque: ",d.size())

print("It;s empty, yeah?", d.isEmpty())

myDeque.enqueue("hello")

