def twoSum(nums, target):
    numsDict = {}

    for i in range(len(nums)):
        if target - nums[i] in numsDict: 
            return([numsDict[target - nums[i]], i])
        else: 
            numsDict[nums[i]] = i
    return


print(twoSum([2,7,11,15], 22))