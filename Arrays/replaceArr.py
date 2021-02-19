'''
Given an array arr[] of n elements, the task is to replace all the odd positioned elements with their cubes and even positioned elements with their squares i.e. the resultant array must be {arr[0]3, arr[1]2, arr[2]3, arr[3]2, …}.

Input: arr[]= {2, 3, 4, 5}
Output: 8 9 64 25

'''

def replace(arr):
    for i in range(len(arr)):
        if (i+1)%2 == 0:
            arr[i] = pow(arr[i],2)
        else: 
            arr[i] = pow(arr[i], 3)
    return arr

print(replace([2,3,4,5]))