# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
        
        L = list(s)
        
        i = 0
        j = len(s) - 1
        
        while i<j:
            
            # while i < j and L[i] not in vowels:
            #     i += 1
            
            # while i < j and L[j] not in vowels:
            #     j -= 1
            if L[i] not in vowels:
                i += 1
            elif L[j] not in vowels:
                j -= 1
            
            else: 
                L[i], L[j] = L[j], L[i]
                
                i += 1
                j -= 1
       
        return (''.join(L))


    def reverseVowelsAnotherWay(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
        
        L = list(s)
        
        i = 0
        j = len(s) - 1
        
        while i<j:
            
            while i < j and L[i] not in vowels:
                i += 1
            
            while i < j and L[j] not in vowels:
                j -= 1
            
            
            
            L[i], L[j] = L[j], L[i]
            
            i += 1
            j -= 1
        
        return (''.join(L))
        
test = Solution()

print(test.reverseVowels("leetcode"))
print("===================================")
print(test.reverseVowelsAnotherWay("leetcode"))