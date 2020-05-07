'''
Write a recursive function which takes an integer and computes the cummulative sum of 0 to that integer.
'''

def recSum(n):
    #Base case
    if n == 0:
        return 0
    else:
        return(n + recSum(n-1))

print(recSum(4))