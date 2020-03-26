# Implementing a Tree Using Lists
# Empty parernthesis are to signify that the node has no children of its own

def binaryTree(r):
	return [r, [], []] # This only creates the root node, nd two empty sublists for the children. 

def insertLeft(root, newBranch):
	tree = root.pop(1) # Pops out the left empty list

	if len(tree) > 1: # If the left subtree has something in it
		root.insert(1, [newBranch, tree, []])
	else:
		root.insert(1, [newBranch, [], []])

	return root

def insertRight(root, newBranch):
	tree = root.pop(2) # Pops out the right empty list
 
	if len(tree) > 1: # If the right subtree has something in it
		root.insert(2, [newBranch, [], tree])
	else:
		root.insert(2, [newBranch, [], []])

	return root

def getRoot(root):
	return root[0]

def setRootVal(root, newVal):
	root.pop(0)

	root.insert(0, newVal)

	return root[0]

def getLeftChild(root):
	return root[1]

def getRightChild(root): 
	return root[2]


r = binaryTree(3)
insertLeft(r,4)
t = insertLeft(r,5)

print(t)

insertRight(r,6)

print(insertRight(r,7))

l = getLeftChild(r)

print(l)
newVal = setRootVal(r,0)

print(newVal)

print(r)
