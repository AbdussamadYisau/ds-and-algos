class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxOnes = 0
        for i in nums:
            if i == 1:
                count += 1
                # maxOnes = max(maxOnes, count) 
                if maxOnes < count:
                    maxOnes = count
                else:
                    maxOnes = maxOnes
            else:
                count = 0
        return maxOnes
# Another method 
def num_of_ones(list_value):
    count = 0
    new = []
    for i in list_value:
        if i == 1:
            count += 1
            new.append(count)  
        elif i == 0:
            count = 0
    return max(new)

          
l1 = [1,1,0,1,1]
l2 = [1,1,1,0,0,0,0,1]
ans =num_of_ones(l2)
print(ans)