class Node(object):
	def __init__(self,value):
		self.value = value # This refers to the element created in the node
		self.nextNode = None # This refers to the "link" to the next element

a = Node(1)
b= Node(2)
c = Node(3)

a.nextNode = b

b.nextNode = c

print(a.value) # Prints the value of variable a.

print(a.nextNode) # Prints the position of the a's next node.


