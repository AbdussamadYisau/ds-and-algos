# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def middleNode(self, head: ListNode):
		n = 1
		copy = head
		while copy.next != None:
			copy = copy.next
			n+=1
		for i in range(n//2):
			head = head.next
		return head

abc = Solution()

abc.middleNode([1,2,3,4,5])
