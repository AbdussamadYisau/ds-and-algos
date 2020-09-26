# Find Odd Numbers between a range of numbers
import time
startTime = time.time()

def oddNumbers(l,r):
    solution = []
    for i in range(l,r+1):
        if i%2 != 0:
            solution.append(i)
    print("--- First Function %s seconds ---" % (time.time() - startTime))
    return solution


def oddNumbersSecondWay(l,r):
    solution = []

    if(l%2 == 0):
        l+=1

    while l < r+1:
        solution.append(l)
        l+=2
    print("--- Second Function %s seconds ---" % (time.time() - startTime))
    return solution

print(oddNumbers(2,5))
print(oddNumbersSecondWay(2,5))