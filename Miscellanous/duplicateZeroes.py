# def duplicateZeroes(arr):
#     s = 0
#     # d stands for destination
#     d = 0

#     destinationArr = []

#     for num in range(len(arr)):
#         if arr[num] == 0:
#             destinationArr[d] = 0
#             d += 1
#             destinationArr [d] = 0
#         else:
#             destinationArr[d] = arr[num]
#         d += 1
        
#     arr = destinationArr
    
#     return arr

# print(duplicateZeroes([1,0,2,3,0,4,5,0]))

def duplicateZeroes(arr):
    #s = 0
    # d stands for arr's length
    d = len(arr)

    destinationArr = []

    for num in range(len(arr)):
        if arr[num] == 0:
            destinationArr.append(arr[num])
            destinationArr.append(arr[num])
           
        else:
            destinationArr.append(arr[num])
        
    arr = destinationArr
    arr = arr[0:d]

    
    return arr
            
print(duplicateZeroes([1,0,2,3,0,4,5,0])) 