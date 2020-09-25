
#Hackerrank Test question with Chekwa
def findNumber(nums, k):
    for i in nums:
        if k == i:
            return("YES")
    return("NO")


print(findNumber([5,1,2,3,4,5], 1))