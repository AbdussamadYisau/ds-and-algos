'''
Arithmetic progression. Number dey miss wey no be first or last element in the progression, return the missing number.
a_{n}=a_{1}+(n-1)d

d = (a_n - a_1)/n-1
3 = 1 + 1*d

TestCase = [1,3,7,9]
1. Count elements in arr
2. d = (a_n - a_1)/n-1
3. 
'''

def arithmethicP(arr):
    n = len(arr)

    commonDiff = (arr[-1] - arr[0])//(n)
    print(commonDiff)
    for i in range(n-1):
        if arr[i] + commonDiff != arr[i+1]:
            return (arr[i]+commonDiff)



print(arithmethicP([1,3,7,9]))

