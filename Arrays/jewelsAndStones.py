# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        output = 0
        for i in S:
            if i in J:
                output += 1
        return output
        
test = Solution()

print(test.numJewelsInStones("aA", "aAAbbbb"))