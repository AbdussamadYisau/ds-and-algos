'''  
BinaryHeap() - creates a new, empty, binary heap.
insert(k) - adds a new item to the heap
findMin() - returns the item with the minimum key value, leaving item in the heap.
delMin() - returns the item with the minimum key value, leaving item in the heap.
isEmpty() - returns true if the heap is empty, false otherwise
size() - returns the number of items in the heap.
buildHeap(list) - builds a new heap from a list of keys

'''

 #List reppresentation

 class BinHeap: 
 	def __init__(self):
 		self.heapList = [0]
 		self.currentSize = 0    
