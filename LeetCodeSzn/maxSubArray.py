def maxSubArrayBruteForce(nums):
    currentSum = nums[0]
    maxSum = nums[0]

    for i in range(0, len(nums)):
        currentSum = 0
        # print(i)
        for j in range(i, len(nums)-1):

            currentSum = max(currentSum + nums[j], nums[j])

            maxSum = max(maxSum, currentSum)
    
    return maxSum

def maxSubArrayEfficient(nums):
    currentSum, maxSum = nums[0], nums[0]


    for num in nums[1:]:
        currentSum = max(currentSum + num, num)
        maxSum = max(maxSum, currentSum)

    return maxSum
    



print(maxSubArrayBruteForce([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArrayEfficient([-2,1,-3,4,-1,2,1,-5,4]))




