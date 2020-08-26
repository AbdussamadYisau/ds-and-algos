# https://leetcode.com/problems/3sum/

def threeSum(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    return(nums[i], nums[j], nums[k])
    return("Ko si result")

print(threeSum([-1, -1 , 2, 3, 3, 3]))
print(threeSum([-3, 3 , 3, 3, 3, 3]))