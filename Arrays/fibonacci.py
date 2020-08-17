# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)
    def memoize(self, N: int) -> []:
        fibArray = [0,1]
        
        for i in range(2, N+1):  
            fibArray.append(fibArray[i-1] + fibArray[i-2])
        return fibArray[-1]

solution = Solution()
print(solution.fib(100))