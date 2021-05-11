#  https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A):
        commonString= list(A[0])
        
        for i in A:
            answerString= []
            for j in i:
                if j in commonString:
                    answerString.append(j)
                    commonString.remove(j)
            commonString = answerString
        
        return commonString
                
                
                
example = Solution()

print(example.commonChars(["bella","label","roller"]))