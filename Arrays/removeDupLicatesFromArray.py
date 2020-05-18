'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

'''

class Solution:
    def removeDuplicates(self, nums):
        
        # array size
        n = len(nums)
        # i is the slower runner in the 2-pointer approach
        i = 0
        # j is the fast runner in the 2-pointer approach
        j = 1
        
        while (j<n):
            # print(nums[i], nums[j])
            if (nums[i] != nums[j]):
                
                i += 1
            nums[i] = nums[j]
            j += 1
            
        return(i+1)
test = Solution()

print(test.removeDuplicates([0,0,1,1,2,2,3,3,4,4,5,5]))