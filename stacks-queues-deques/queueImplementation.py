class Queue(object):
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def  enqueue(self,item):
		return (self.items.append(item))
	def  dequeue(self):
		return (self.items.pop(0))
	def peek(self):
		return self.items[0]
	def size(self):
		return(len(self.items))

# Testing it out 

q = Queue()
print("This is the current size of the queue: ", q.size())
print("Is it empty? True/False: " , q.isEmpty())

q.enqueue(1)
q.enqueue(2)

q.enqueue(3)

q.enqueue(4)

print(q.dequeue())


