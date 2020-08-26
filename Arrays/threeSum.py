# https://leetcode.com/problems/3sum/

#Naive Solution
def threeSum(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    
    
    return res

# Efficient Solution

def threeSumEfficient(nums):
    nums.sort()

    res = []

    print(nums.sort())

    for i in range(len(nums)):

        #Two-pointer method to find the other characters

        secondNum = i + 1

        lastNum = len(nums) - 1

        while (secondNum < lastNum):
            if(nums[i] + nums[secondNum] + nums[lastNum] == 0):
                res.append([nums[i], nums[secondNum], nums[lastNum]])
            elif (nums[i] + nums[secondNum] + nums[lastNum] < 0):
                secondNum += 1
            else:
                lastNum -= 1
    return res

print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([-3, 3 , 3, 3, 3, 3]))
print("==============================================")
print(threeSumEfficient([-1, 0, 1, 2, -1, -4]))