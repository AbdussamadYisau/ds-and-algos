# This solution's time complexity is O(N^2)

def printAllSubarrays(arr,n):
	#Consider all sub-arrays starting from i
	for i in range(0,n):
		sum = 0 #tracker for sum of elements
		

		for j in range(i,n):
			#Sum of elements so far

			sum += arr[j]

			if(sum == 0):
				print("Subarray [{i}..{j}]".format(i = i, j =j))


arr = [3,4,-7,3,1,3,1,-4,-2,-2]
n = len(arr)

printAllSubarrays(arr,n)



# This solution's time complexity is O(N)
# def printAllSubarrays(arr, n):

#     hashMap = {}

#     #Create an array to hold the sub arrays

#     hold = []

#     #tracker for sum of elements

#     sum = 0

#     for i in range(n):
#         sum += arr[i]

#         #If sum is 0, we have successfully found a subarray starting from index 0 and ending at index I

#         if sum == 0:
#             hold.append((0,i))

#         alreadyExists = []
        
#         #Check if sum exists in hashmap already
#         if sum in hashMap: 
#             alreadyExists = hashMap.get(sum)
#             alreadyExistLength = len(alreadyExists)
#             for ele in range(alreadyExistLength):
#                 hold.append((alreadyExists[ele] + 1, i))
#         alreadyExists.append(i)
#         hashMap[sum] = alreadyExists
    
#     print(hold)


# arr = [3,4,-7,3,1,3,1,-4,-2,-2]
# n = len(arr)

# printAllSubarrays(arr,n)

# #Trying out hashmap now






































































