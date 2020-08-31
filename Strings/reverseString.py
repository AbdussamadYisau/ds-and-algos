# A LeetCode question - Solved with the two pointer approach. It was supposed to be solved in-place

class Solution():

    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        
        while (i < j):
            s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1
        return s  #If this is removed, it would be in-place. I included it so that we can see if it does what it is supposed to.

l = Solution()
print(l.reverseString(["H","e", "l", "l", "o"]))