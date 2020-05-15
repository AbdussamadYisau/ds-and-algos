class Solution:
    def containsDuplicate(self, nums):
        myDict = {}
        
        for ele in nums:
            if ele not in myDict:
                myDict[ele] = 1
            else: 
                return True
        return False
        