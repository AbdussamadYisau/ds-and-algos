def squareDigitSum(n):
	 return sum(map(lambda x:int(x)**2, str(n)))


def happyNumber(n):
	"""
	A happy number is a number defined by the following process: 
	Starting with any positive integer, replace the number by the sum of the squares of its digits,
	 and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
	Those numbers for which this process ends in 1 are happy numbers.

	Input: 19
	Output: True


	"""

	while True:

		if(n == 1):
			return True


		# Replace n with sum of digit square if n is not 1

		n = squareDigitSum(n)

		if (n == 4):
			return False

	return False





#print(happyNumber(10))

print(happyNumber(10))
