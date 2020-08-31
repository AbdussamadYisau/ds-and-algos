#  https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        myDict = {}
        
        for i in s:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 0
        for k in myDict:
            if myDict[k] == 0:
                return s.find(k)
        return(-1)
        
test = Solution()

print(test.firstUniqChar('loveleetcode'))
        
        

          

          
        