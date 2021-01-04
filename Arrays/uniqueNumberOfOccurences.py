'''

https://leetcode.com/problems/unique-number-of-occurrences/

'''

def uniqueNumberOfOccurence(arr):
    myDict = {}

    valArray =[]

    for i in arr:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1

    for val in myDict.values():
        valArray.append(val)

    return (len(set(valArray)) == len(valArray))


print(uniqueNumberOfOccurence([1,2,2,1,1,3]))