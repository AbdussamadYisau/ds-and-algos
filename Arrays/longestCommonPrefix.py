# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        
        current = strs[0]
        
        for i in range(1,len(strs)):
            temp = ""
            
            for j in range(len(strs[i])):
                
                if j<len(current) and current[j] == strs[i][j]:
                    temp += current[j]
                else:
                    break
            current = temp
        return current
            
                
        
        
        