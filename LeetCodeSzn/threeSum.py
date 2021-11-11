# https://leetcode.com/problems/3sum/

#Naive Solution
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if (i>0 and nums[i]==nums[i-1]): 
            continue
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    
    
    return res

# Efficient Solution
def threeSumEfficient(nums):
    res =[]
    nums.sort()

    arrLength = len(nums)

    for i in range(arrLength-2):

        if (i>0 and nums[i]==nums[i-1]): 
            continue
        left = i+1
        right = arrLength-1

        while left < right:
            total = nums[i]+nums[left]+nums[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:
                res.append([nums[i], nums[left], nums[right]])

                while left<right and nums[left]==nums[left+1]:
                    left += 1
                while left<right and nums[right]==nums[right-1]:
                    right -= 1
                left += 1
                right -= 1

            
    return res
                
print(threeSumEfficient([-1, 0, 1, 2, -1, -4]))

print("=============================")


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([-3, 3 , 3, 3, 3, 3]))
print("==============================================")
# print(threeSumEfficient([-1, 0, 1, 2, -1, -4]))