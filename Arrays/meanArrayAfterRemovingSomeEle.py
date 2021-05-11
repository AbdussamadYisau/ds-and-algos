# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
class Solution:
    def trimMean(self, arr):
        arr.sort()
        
#         5% 
        fivePercent = int((len(arr)*5 / 100))
        
        arr = arr[fivePercent:len(arr) - fivePercent]
        
        return (sum(arr)/len(arr))


example = Solution()

print(example.trimMean([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))
            
        