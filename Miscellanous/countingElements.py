def countElements(arr):
    count = {}
    for i in arr:
        count[i] = count.get(i,0) + 1
    total = 0

    for k,v in count.items():
        if k + 1 in count:
            total += v
    #print(count.items())
    return total

arr = [1,2,3]

print(countElements(arr))
