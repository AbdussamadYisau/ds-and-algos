# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution(object):
   def gcdOfStrings(self, str1, str2):
      if len(str1)<=len(str2):
         temp = str1
      else:
         temp = str2
      m = len(temp)
      x = 1
      res=[""]
      while x<=m:
         if m%x==0 and temp[:x] * (len(str1)//x) == str1 and temp[:x] * (len(str2)//x) == str2:
            res.append(temp[:x])
            
         x+=1
      return res[-1]
ob1 = Solution()
print(ob1.gcdOfStrings("ABABAB","ABAB"))

#Efficient solution
class SolutionTwo:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            if a == 0:
                return b
            else:
                return gcd(b%a, a)
        d = gcd(len(str1), len(str2))
        return str1[: d] if str1[: d] * (len(str2) // d) == str2 and str2[: d] * (len(str1) // d) == str1 else ''
                