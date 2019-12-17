row, col = 6, 6
Hrow = Hcol = max = 0

index = 1;

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

#print out the array to see the elements in it
for row in arr: 
    print(row)

print("\n") #leave to newline for readability

#loop to print out all necessary output
while 1 : 
	sum = 0 # variable sum is declared in the loop to reset all saved value
	
	print("Hourglass {}:".format(index))
	
	#to make this loop function as ut should, the maximum range must be 6 for both row and col
	for row in range(Hrow , 3 + Hrow):
		for col in range(Hcol, 3 + Hcol):
			
			#this is to skip the two side array
			if (row == 1 + Hrow) and ( (col == 0 + Hcol) or (col ==2 + Hcol) ):
				print(" ",end = ' ')
				continue
			
			print(arr[row][col],end = ' ')#print array element
			sum = sum + arr[row][col] #add the element to sum
		print()#go to the next row
		
	print("Sum of element is:", sum) #print sum
	
	if sum > max : #check if sum is the max
		max = sum
		
	print("\n")
	
	Hcol = Hcol + 1#increment Hcol by 1
	
	if Hcol >= 4 :#make sure it doesnt pass 3
		Hcol = 0 #rest the value for the next loop
		Hrow = Hrow + 1 #increment Hrow
		
	if Hrow >= 4: #make sure it doesnt pass 3
		break  #break out of the while loop if Hrow = 4
		
	index = index + 1

print("The maximum sum of elements in Hourglass array is:", max)