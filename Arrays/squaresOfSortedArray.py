# This fails for large inputs, because remove is O(n). It also fails for courses where there are not unique numbers
class Solution:
    def sortedSquares(self, nums):
        ans = []
        
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        for i in range(len(nums)):
            ans.append(min(nums))
            nums.remove(min(nums))
        return ans

t = Solution()

print(t.sortedSquares([-4,-1,0,3,10]))

class SolutionOne:
    def sortedSquares(self, nums):
        n = len(nums)
        left, right = 0, n - 1
        index = n - 1
        result = [0 for x in nums]
    
        while index >= 0:
    
            if abs(nums[left]) >= abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        
        for i in range(n): 
            nums[i] = result[i]

        return nums
        

s = SolutionOne()

print(s.sortedSquares([-4,-1,0,3,10]))      
        