class Solution:
    def maxProductBruteForce(self, nums):
        
        maxSeq = nums[0]
        
        for i in range(0, len(nums)):
            currProd = nums[i]
            for j in range(i+1, len(nums)):
                
                currProd *= nums[j]
                maxSeq=max(maxSeq, currProd)
                
                if maxSeq < nums[j]:
                    maxSeq = nums[j]
        return maxSeq
    def maxProduct(self, nums):
        
        result, maxVal, minVal = max(nums), 1, 1
        
        for num in nums:
            tmp = maxVal
            
            maxVal = max(num, tmp*num, minVal*num)
            minVal = min(num, tmp*num, minVal*num)
            result = max(result, maxVal, minVal)
            
        return result

            
            
            
        
            
            
        