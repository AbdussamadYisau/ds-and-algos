class Solution:
    def twoSum(self, numbers, target):
        numsDict = {}
        
        for i in range(len(numbers)):
            if target - numbers[i] in numsDict: 
                return([numsDict[target - numbers[i]] + 1, i + 1])
            else: 
                numsDict[numbers[i]] = i
        return
    
    def twoSumsSlidingWindow(numbers, target):

        leftPointer = 0
        rightPointer = len(numbers)-1

        while leftPointer < rightPointer:

            if numbers[leftPointer] + numbers[rightPointer] > target:
                rightPointer -= 1
            elif numbers[leftPointer] + numbers[rightPointer] < target:
                leftPointer += 1
            
            if numbers[leftPointer] + numbers[rightPointer] == target:
                return([leftPointer + 1, rightPointer + 1])


print(Solution.twoSumsSlidingWindow([-1, 0], -1))