# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# BruteForce

class BruteForceSolution:
    def smallerNumbersThanCurrent(self, nums):
        answer = []
        
        
        for num in nums:
            counter = 0
            for i in range(len(nums)):
                if nums[i] < num:
                    counter += 1
            answer.append(counter)
            
        return answer

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        answer = []
        
        sortedNums = sorted(nums)
        
        for num in nums:
            answer.append(sortedNums.index(num))
        return answer
    
                
                
        
                
                
example = BruteForceSolution()
exampleTwo = Solution()


print(example.smallerNumbersThanCurrent([8,1,2,2,3]))

print(exampleTwo.smallerNumbersThanCurrent([8,1,2,2,3]))
