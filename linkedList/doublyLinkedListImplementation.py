# Implementation of a doubly linked list

class doublyLinkedListNode(object):
	def __init__(self,value):

		self.value = value
		self.nextNode = None
		self.prevNode = None



a = doublyLinkedListNode(1)
b = doublyLinkedListNode(2)
c = doublyLinkedListNode(3)


a.nextNode = b
b.prevNode = a
b.nextNode = c
c.prevNode = b


print(a)

print(a.prevNode)

print(a.nextNode)

print(b)
