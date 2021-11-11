class Solution:
    def lengthOfLongestSubstring(s):
        longestSubstring = []
        
        maxLen= 0
        
        n = len(s)
    
        
        for i in range(n): 
            
            longString = ""
            
            for j in range(i,n):

                if s[j] in longString:
                    longestSubstring.append(longString)
                    longString = s[j]

                else:
                    longString += s[j]
        
            longestSubstring.append(longString)
        
        for i in longestSubstring:
            maxLen=max(len(i), maxLen)
            
       
        return maxLen


s = 'pwwkew'

print(Solution.lengthOfLongestSubstring(s))
        
        