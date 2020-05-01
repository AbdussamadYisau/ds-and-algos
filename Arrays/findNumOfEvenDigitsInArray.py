class Solution:
    def findNumbers(self, nums: List[int]) -> int:
#         ans = 0
#         count = 0
        
#         for num in nums:
#             while num != 0:
#                 num //= 10 
#                 count += 1
#             if count % 2 == 0:
#                 ans += 1
                
#         return ans
        ans = 0
        
        for num in nums:
            
            if(len(str(num)) % 2 == 0):
                ans += 1
        return ans
            
        