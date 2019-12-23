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
		pass
	def insertAtEnd(self,data):
		pass
	def createList(self):
		pass
	def insertBefore(self,data,x):
		pass
	def insertAtPosition(self,data,k):
		pass
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







 
