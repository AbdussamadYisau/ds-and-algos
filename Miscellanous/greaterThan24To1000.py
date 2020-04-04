def greaterThan24(n):


	arr =[]
	while n >= 5:

		if n % 5 == 0:
			divide = n/5

			arr += [5]*int(divide)

#			arr += [5 for i in range(divide)]

			return arr

		elif n % 7 == 0:
			divide = n / 7

			arr += [7]*int(divide)

#			arr += [7 for i in range(divide)]

			return arr

		else:
			arr.append(7)
			n -= 7

print(greaterThan24(38))
