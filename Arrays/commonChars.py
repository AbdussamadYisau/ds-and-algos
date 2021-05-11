#  https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A):
        commonList= list(A[0])
        
        for i in A:
            answerString= []
            for j in i:
                if j in commonList:
                    answerString.append(j)
                    commonList.remove(j)
            commonList = answerString
        
        return commonList
                
                
                
example = Solution()

print(example.commonChars(["bella","label","roller"]))