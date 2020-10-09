from functools import cmp_to_key
class Solution:
    def comparator(a,b):
        if a[0]<b[0]:
            return -1
        else:
            return 1
    def merge(self, intervals):
        data = sorted(intervals, key=cmp_to_key(Solution.comparator))
        answer = []
        
        if (len(data) == 0):
            return answer
        start = data[0][0]
        end = data[0][1]
        for i in range(1,len(data)):
            if end >= data[i][0] and end < data[i][1]:
                end = data[i][1]
            if end < data[i][0]:
                answer.append([start,end])
                start = data[i][0]
                end = data[i][1]
        answer.append([start,end])

        return answer
        
test = Solution()

print(test.merge([[1,3],[2,6],[8,10],[15,18]]))
print(test.merge([[1,4],[4,5]]))
