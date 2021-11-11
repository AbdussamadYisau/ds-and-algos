def containsDuplicates(nums, k, t):
    i = 0
    j = len(nums) - 1

    # nums.sort()

    if k == 0: 
        return False
    
    if k < 0 or t < 0:
        return False

    while i < j:

        # print(i,j)

        if abs(i-j) <= k and abs(nums[i] - nums[j]) <= t:
            print(i,j)
            return True
        if abs(i-j) > k and abs(nums[i] - nums[j] >t):
            i = i + 1
        else: 
            j = j - 1

    # for i in range(0,len(s)):
        


    print(i,j)
    return False

print(containsDuplicates([1,5,9,1,5,9],
2,
3))