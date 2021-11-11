class Solution:
    def powerXtoN(self, x, n):
        return x**n
    def powerBruteForce(self, x, n):
        if x < 0 and n%2 != 0:
            x = abs(x)
            return -(x**n)
        else: 
            return x**n