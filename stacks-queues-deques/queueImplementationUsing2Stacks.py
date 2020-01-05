class Queue2Stack(object):
	def __init__(self):
		# Declare the two stacks
		self.instack = []
		self.outstack = []

	def enqueue(self,item):
		return(self.instack.append(item))

	def dequeue(self):
		if self.outstack == []:
			while not self.instack == []:
				popped = self.instack.pop()
				self.outstack.append(popped)
		return self.outstack.pop()


Q2S = Queue2Stack()

Q2S.enqueue(1)
Q2S.enqueue(2)
Q2S.enqueue(3)
Q2S.enqueue(4)

print(Q2S.dequeue())


