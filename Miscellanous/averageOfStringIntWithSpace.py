def averageOfStringInt(string):
    listString = string.split()
    average = 0
    for num in listString:
        numInt = int(num)
        
        average += numInt
    average = average / len(listString)
    
    return average

print(averageOfStringInt("1 2 45 2 8 2"))