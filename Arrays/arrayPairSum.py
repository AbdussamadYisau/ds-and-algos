# Given an integer array, output all the unique pairs that sum up to a specific value k.

# So the input:

# pair_sum([1,3,2,2],4)

# would return 2 pairs:

#  (1,3)
#  (2,2)

def pairSum(arr,n, sum): 
	count = 0 #Initializing the count of the number of pairs
	for i in range(0,n):
		for j in range(i+1,n):
			if arr[i] + arr[j] == sum:
				count += 1
	return count
	
# def thePairs(arr,n, sum): 
# 	count = 0
# 	for i in range(0,n):
# 		for j in range(i+1,n):
# 			if arr[i] + arr[j] == sum:
# 		 		count +=1
# 		 		print ([(arr[i], arr[j])])
		        
# 	return ("The number of pairs is: ",count)


def thePairs(arr,n, sum):
	diff_pairs = [(arr[i], sum-arr[i]) for i in range(0, n) if sum-arr[i] in arr]

	return ("The pairs are: ", diff_pairs) 





arr = [1,5,7,-1,5]
n = len(arr)
sum = 6

print("Count of pairs is: ", pairSum(arr,n,sum))

print (thePairs(arr,n, sum))