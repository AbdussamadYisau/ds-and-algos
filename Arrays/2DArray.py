'''
Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

hourglassSum has the following parameter(s):

arr: an array of integers
'''


row = 6
col = 6

arr = [[0 for i in range(col)] for j in range(row)] 
  
# again in this new array lets change 
# the first element of the first row  
# to 1 and print the array 
arr[0][0] = 1 
arr[0][1] = 1
arr[0][2] = 1 

arr[1][1] = 1

arr[2][0] = 1 
arr[2][1] = 1
arr[2][2] = 1

arr[3][2] = 2 
arr[3][3] = 4
arr[3][4] = 4

arr [4][3] = 2

arr[5][2] = 1
arr[5][3] = 2
arr[5][4] = 4


# def hourglassSum(arr):

# # start max_hourglass_sum at smallest possible hourglass
# 	max_hourglass_sum = -63  

# 	def __get_hourglass_sum(arr, row, col):
# 		sum = 0
# 		sum += matrix[row-1][col-1] # top left
# 		sum += matrix[row-1][col]  # top center
# 		sum += matrix[row-1][col+1] # top right
# 		sum += matrix[row][col] # lone center
# 		sum += matrix[row+1][col-1] #bottom left
# 		sum += matrix[row+1][col] # bottom center
# 		sum += matrix [row+1][col+1] #bottom right

# 		return sum

# 	for i in range(1,5):
# 	    for j in range(1, 5):
# 	        current_hourglass_sum = _get_hourglass_sum(arr, row, col)
# 	        if current_hourglass_sum > max_hourglass_sum:
# 	            max_hourglass_sum = current_hourglass_sum

# 	print(max_hourglass_sum)



# hourglassSum(arr)





