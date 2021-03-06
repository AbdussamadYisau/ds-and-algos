# # Add One 
# # Example 1

# # Input: [1,2,3] ->> 123 + 1 =>> 124 => [1,2,4]
# # Output: [1,2,4]

# # Explanation: The array represents the integer 123.

# # Example 2 

# # Input: [4,3,2,1]
# # Output: [4,3,2,2]
# # Explanation: The array represents the integer 4321.

# # How I went about it, converted list to int, added 1, and converted int back to list.



# def addOne(test_array) : 
#     for i in range(0,len(test_array)): 
#         test_array[i] = str(test_array[i])
    
#     string_rep = "";
#     for i in range(0, len(test_array)):
#         string_rep += test_array[i]
        
#     string_rep = int(string_rep)
#     string_rep += 1

    
#     newArray = [int(i) for i in str(string_rep)]
    
#     return newArray


# print ("This is the new array:", addOne([9,9,9,9]))

# print ("This is the new array:", addOne([1,2,3]))

# print ("This is the new array:", addOne([1,2,9,9]))

def plusOne(digits):
    res = []
    carry = 1
    
    for d in digits[::-1]:
        res.append((d+carry)%10)
        carry = (d+carry) // 10

        # print(res,carry)
    
    if carry:
        res.append(carry)
        
    return res[::-1]

print(plusOne([9,8,9]))