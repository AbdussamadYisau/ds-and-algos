class Solution:
    def maxSubArray(self, nums):
        max_seq = nums[0]
        curr_sum = nums[0]
        for num in nums[1:]:
            if curr_sum <= 0:
                curr_sum = num
            else:
                curr_sum += num
            if curr_sum > max_seq:
                max_seq = curr_sum
        return max_seq
            
            
example = Solution()


                
        
nums = [-2,1,-3,4,-1,2,1,-5,4]          

print(example.maxSubArray(nums))
