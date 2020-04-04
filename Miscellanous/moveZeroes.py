# def moveZeroes(arr):
# 	return ([nonZero for nonZero in arr if nonZero!=0] + [Zero for Zero in arr if Zero==0]) 


# print(moveZeroes([1,0,2,4,39,5,0,0,0])

def moveZeroes(arr):
	nonZeroList = [nonZero for nonZero in arr if nonZero != 0]
	zeroList = [zero for zero in arr if zero == 0]

	return(nonZeroList + zeroList)

arr = [1,0,2,4,39,5,0,0,0]

print(moveZeroes(arr))

def moveZeroesInPlace(arr):
	arr[:] = [x for x in arr if x != 0 ] + [0]* arr.count(0)

	return arr

print(moveZeroesInPlace(arr))
