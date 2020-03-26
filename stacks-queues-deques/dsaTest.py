# QUESTION 2 - ORDERING AN ARRAY.
# Imagine if you had a large array of numbers being updated by some server process. Normally, the
# array is meant to be sorted, but, due to some errors, some numbers are out of place.
# However, you are certain that each number is away from it’s correctly sorted index by at most K.
# For example, if a number is at position 3, you can be sure that it’s position if the array is perfectly
# sorted, the number is going to fall between the index range of 3-K and 3+K
# Design an algorithm that can sort this array of logs efficiently.
# Sorting the array is an obvious solution which takes O(n log n), we are looking for a better
# algorithm than that.
# Input : arr = {6, 5, 3, 2, 8, 10, 9}
# K= 3
# Output : arr[]= {2, 3, 5, 6, 8, 9, 10}
# Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
# K = 4
# Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
def order_Karray(arr):
	for i in range(1, len(arr)):
		currentValue = arr[i]
		position = i 

		while position > 0 and arr[position - 1] > currentValue:
			arr[position] = arr[position - 1]
			position = position - 1

		arr[position] = currentValue


arr = [6, 5, 3, 2, 8, 10, 9]

order_Karray(arr)
print(arr)




# QUESTION 1 - IMPLEMENT A BROWSER NAVIGATOR
# Design a data structure that emulates the browser history navigation functionality of a typical
# web browser. You should support the following methods :
# ● get_current_url() // returns the current URL you are on
# ● go_to(URL) // navigates to a new URL which is passed in
# ● back() // navigates you to a previous URL before the current URL. handle cases where no
# previous URL exists
# ● forward() // navigates you to the next URL after the current URL. handle cases where no
# forward URL exists
# ● jump_to(URL) // this jumps your browser current location to a specific URL which must
# have been visited before
# Follow Up - Can you make all operations work in O(1)?
# BrowserHistory bh = new BrowserHistory( );
# bh.get_current_url() // returns None
# bh.go_to(“www.google.com”) // navigates to google.com
# bh.get_current_url() // returns “www.google.com”
# bh.go_to(“www.twitter.com”) // navigates to twitter.com
# bh.go_to(“www.twitter.com/dsalagos”) //navigates to www.twitter.com/dsalagos
# bh.back() // goes back
# bh.get_current_url() // returns “www.twitter.com”
# bh.forward()
# bh.get_current_url() // returns “www.twitter.com/dsalagos”
# bh.jump_to(“www.google.com”) // jumps back to “www.google.com”
# bh.forward() // moves forward to www.twitter.com, as this is the next url after we added
# “www.google.com”

class web_browser(object):
	def __init__(self):
		self.url = None
	def get_current_url(self):
		print(self.url)
	def go_to(self, url):  
		self.url = url
		print(self.url)
