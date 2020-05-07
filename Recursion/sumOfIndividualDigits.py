'''
Given an integer, create a function which returns the sum of all the individual digits in that integer.
For example: If n = 4321, return 4 + 3 + 2 + 1
'''
def sumFunct(n):
    sumOfInts = 0

    if n == 0:
        return 0

    else:

        sumOfInts = n%10

        sumOfInts = sumOfInts + sumFunct(n//10)
        return (sumOfInts)

print(sumFunct(4321))
print(sumFunct(687))
