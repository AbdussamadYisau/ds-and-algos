# https://leetcode.com/problems/partition-labels/

class Solution(object):
    def partitionLabels(self, S):
        last = {value: key for key, value in enumerate(S)}
        print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans

test = Solution()
# print(test.partitionLabels("abbcbcdefegdehijhklij"))
print(test.partitionLabels("ababcbacadefegdehijhklij"))