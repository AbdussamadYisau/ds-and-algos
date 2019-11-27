'''
Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

hourglassSum has the following parameter(s):

arr: an array of integers
'''


rows, cols = (6, 6) 

arr = [[0 for i in range(cols)] for j in range(rows)] 
  
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




for row in arr: 
    print(row) 
