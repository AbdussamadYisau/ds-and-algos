'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

'''

def rotateArr(nums, k):
    i = 0

    while i < k:
        lastNum = nums.pop()

        nums = [lastNum] + nums

        i += 1
    return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(rotateArr(nums,k))

#This is an inplace solution for LeetCode

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         i = 0
#         newNums = nums

#         while i < k:
#             lastNum = newNums.pop()

#             newNums = [lastNum] + newNums

#             i += 1
#         nums[:] = newNums[:]