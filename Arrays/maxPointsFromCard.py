# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

def maxScore(arr, k):
    n = len(arr)
    
    noOfRemoval = n - k
    
    sumOfArray = sum(arr)
    
    print(sumOfArray)
    
    answer = 0
    
    
    for i in range(n):
        
        # if (((i + noOfRemoval) - i ) == k):
        if(i+noOfRemoval < n):
            sumOfRemoval = sum(arr[i:(i + noOfRemoval)])
            answer = max(answer, sumOfArray - sumOfRemoval)
        else:
            return answer 
        
        
        
        
        print(sumOfRemoval, answer, i)
        print('------')
    
    return answer


print(maxScore([1,2,3,4,5,6,1], 3))