#Representing A Tree using Nodes and References

class BinaryTree(object):

	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t 

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
 		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key


r = BinaryTree(0)

print(r.getRootVal())

r.insertLeft(1)
r.insertLeft(1)
r.insertLeft(1)
r.insertLeft(1)
r.insertLeft(1)

r.insertRight(2)
r.insertRight(2)
r.insertRight(2)
r.insertRight(2)
r.insertRight(2)

print(r.getLeftChild()) # This only shows the position. As per reference.

print(r.getLeftChild().getRootVal()) # Herein, we are dealing with subtrees. So the get RootVal treats the leftRootChild as a root Node
# Playing around with the preorder traversal
def preorder(tree):
	if tree != None:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

preorder(r)
