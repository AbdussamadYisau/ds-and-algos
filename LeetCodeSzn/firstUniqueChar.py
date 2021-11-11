class Solution:
    def firstUniqChar(self, s):
        dict = {}
        
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
                
            else:
                dict[s[i]] = 1
        for key, value in dict.items():
            if value == 1:
                return s.index(key)
        return -1
                
                
            
        