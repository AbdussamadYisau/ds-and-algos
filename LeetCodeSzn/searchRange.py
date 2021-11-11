class Solution:
    def searchRange(self, nums, target):
        start, end = -1, -1
        output = []
        
        if target in nums:
            start = nums.index(target)
            
        for i in range(len(nums)):
            if nums[i] == target and i > end:
                end = i
                
        output.append(start)
        output.append(end)

        return output
        