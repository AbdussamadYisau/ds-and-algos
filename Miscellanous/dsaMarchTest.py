def assignTasks(arr):
	subsetOne = []
	subsetTwo = []

	sum_subsetOne = 0
	sum_subsetTwo = 0

	for i in sorted(arr, reverse = True):
		if sum_subsetOne < sum_subsetTwo:
			subsetOne.append(i)
			sum_subsetOne = sum_subsetOne + i
		else:
			subsetTwo.append(i)
			sum_subsetTwo = sum_subsetTwo + i

	print(subsetOne)
	print(subsetTwo)

	if sum_subsetOne == sum_subsetTwo:
		print("True")
	else:
		print("False")


arr = [1,2,3,4]
assignTasks(arr)

print("----------------------------")
arr = [1,2,3,4,5]
assignTasks(arr)
