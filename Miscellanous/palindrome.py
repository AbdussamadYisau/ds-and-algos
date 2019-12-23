# A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.
""""
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"

"""

class Solution: 
    def longestPalindrome(self, s):
    	for i in s:
    		if s[i:] == s[i::-1]:
    			print("Longest palindrome here")
    		else:
    			print("No palindrome.")
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar


