'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# Brute Force Solution

# def twoSum(nums, target):
    
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return(i,j)

# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums,target))

# Optimized solution - Hashmap

def twoSum(nums, target):
    dictionary = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dictionary:
            return(dictionary[complement], i)
        else:
            dictionary[nums[i]] = i
            
nums = [2,7,11,15]
target = 22
print(twoSum(nums,target))