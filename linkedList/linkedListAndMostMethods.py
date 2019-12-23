# This is the implementation of a singly linked  list

class Node:
	def __init__(self,value):
		self.info = value # This refers to the actual data in the node
		self.link = None # This refers to the "link"

class singleLinkedList:
	def __init__(self):
		self.start = None
	def displayList(self):
		if self.start is None:
			print("List is empty")
			return
		else:
			print("List is:    ")
			p = self.start
			while p is not None:
				print(p.info, sep = " ", end = ",")
				p = p.link
			print()
	def countNodes(self):
		p = self.start
		n = 0

		while p is not None:
			n+= 1
			p = p.link
		print("Number of nodes in the list: ", n)
	def search(self,x):
		position = 1 # Initializing position of the default position 
		p = self.start
		while p is not None:
			if p.info == x:
				print(x, " is at position", position)
				return True
			position += 1
			p = p.link
		else:
			print(x, " not found in list." )
			return False 

	def insertInBeginning(self,data):
		temp = Node(data)
		temp.link = self.start
		self.start = temp
	def insertAtEnd(self,data):
		temp = Node(data)
		if self.start is None:
			self.start = temp
			return
		p = self.start
		while p.link is not None:
			p = p.link
		p.link = temp

	def createList(self):
		n = int(input("Enter the number of nodes:  "))
		if n == 0:
			return
		for i in range(n):
			data = int(input("Enter the element to be inserted: "))
			self.insertAtEnd(data)

	def insertAfter(self,data,x):
		p = self.start

		while p is not None: 
			if p.info == x:
				break
			p = p.link

		if p is None:
			print(x, " is not present in the list.")
		else: 
			temp = Node(data)
			temp.link = p.link
			p.link = temp

	def insertBefore(self,data,x):
		p = self.start

		if p is None: 
			print("List is empty.")
			return
		# x is in first node, new node is to be inserted before first node. This is like a a trivial but very important case.

		if p.info == x:
			temp = Node(data)
			temp.link = p
			p = temp
			return
		# Find reference to predecessor of node containing x

		while p.link is not None:
			if p.link.info == x:
				break
			p = p.link
		if p.link is None:
			print(x, " is not present in the list.")
		else:
			temp.link = p.link
			p.link = temp


	def insertAtPosition(self,data,k):
		p = self.start
		if k == 1:
			temp = Node(data)
			temp.link = p 
			p = temp
			return

		i = 1
		while i < k -1 and p is not None: #Find a reference to k-1 node
			p = p.link
			i += 1
		if p is None:
			print("You can insert only upto position", i)
		else: 
			temp = Node(data)
			temp.link = p.link
			p.link = temp

	def deleteNode(self,x):
		pass
	def deleteFirstNode(self):
		pass
	def deleteLasttNode(self):
		pass
	def reverseList(self):
		pass
	def bubbleSortExdata(self): # By exchanging data
		pass
	def bubbleSortExlinks(self): # By exchanging links
		pass
	def hasCycle(self):
		pass
	def findCycle(self):
		pass
	def removeCycle(self):
		pass
	def insertCycle(self):
		pass
	def merge2(self,list2):
		pass
	def _merge2(self,p1, p2):
		pass
	def mergeSort(self):
		pass
	def _mergeSortRec(self, listStart):
		pass
	def _divideList(self, p):
		pass


list = singleLinkedList()

list.createList()

while True: 
	print("1. Display List.")
	print("2. Count the number of nodes.")
	print("3. Search for an element.")
	print("4. Insert in empty list/ insert in beginning of the list.")
	print("5. Insert a node at the end of the list.")
	print("6. Insert a node after a specified node.")
	print("7. Insert a node before a specified node.")
	print("8. Insert a node at a given position")
	print("9. Delete the first node.")
	print("10. Delete last node.")
	print("11. Delete any node.")
	print("12. Reverse the list.")
	print("13. Bubble sort by exchanging data.")
	print("14. Bubble sort by exchanging links.")
	print("15. Merge sort.")
	print("16. Insert cycle.")
	print("17. Delete cycle.")
	print("18. Remove cycle.")
	print("19. Quit.")

	option = int(input("Enter your choice:  "))

	if option == 1:
		list.displayList()
	elif option == 2:
		list.countNodes()
	elif option == 3:
		data = int(input("Enter the element that you want to search for: "))
		list.search(data)
	elif option == 4:
		data = int(input("Enter the element to be inserted: "))
		list.insertInBeginning(data)
	elif option == 5:
		data = int(input("Enter the element to be inserted: "))
		list.insertAtEnd(data)
	elif option==6:
		data=int(input("Enter the element to be inserted: "))
		x=int(input("Enter the element after which to insert: "))
		list.insertAfter(data,x)
	elif option==7:
		data=int(input("Enter the element to be inserted: "))
		x=int(input("Enter the element before which to insert: "))
		list.insertBefore(data,x)
	elif option==8:
		data=int(input("Enter the element to be inserted: "))
		k=int(input("Enter the position at which to insert: "))
		list.insertAtPosition(data,k)

