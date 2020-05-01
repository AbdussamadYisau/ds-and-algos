class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxOnes = 0
        for i in nums:
            if i == 1:
                count += 1
                # maxOnes = max(maxOnes, count) 
                if maxOnes < count:
                    maxOnes = count
                else:
                    maxOnes = maxOnes
            else:
                count = 0
        return maxOnes