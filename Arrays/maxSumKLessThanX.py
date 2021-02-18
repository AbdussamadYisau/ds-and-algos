'''
Given an array arr[] and two integers K and X, the task is to find the maximum sum among all subarrays of size K with the sum less than X.
'''

# Brute Force - O(n*k)

def bruteMaxSumKLessThanX(arr, k, x):

    n = len(arr)

    if n < k:
        return -1
    
    max_sum = 0
    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i+j]
        if current_sum < x and current_sum > max_sum:
            max_sum = current_sum
    return max_sum

print(bruteMaxSumKLessThanX([20, 2, 3, 10, 5], 3,20))


def maxSumKLessThanX(arr, k, x):
    n = len(arr)

    if n < k:
        return -1
    
    window_sum = sum(arr[:k])

    if window_sum < x:
        max_sum = window_sum
    else:
        max_sum = 0
    
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]

        if window_sum < x and window_sum > max_sum:
            max_sum = window_sum
    return max_sum

print("==============")
print(maxSumKLessThanX([20, 2, 3, 10, 5], 3,20))

