def squareDigitSum(n):
	 return sum(map(lambda x:int(x)**2, str(n)))


def happyNumber(n):

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
