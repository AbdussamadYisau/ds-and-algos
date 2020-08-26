# https://www.hackerrank.com/challenges/save-the-prisoner/problem

#Naive solution

def saveThePrisoner(n, m, s):
    count = s

    for _ in range(m - 1):
        if (count >= n):
            count = 1
        else:
            count += 1
    return count

print(saveThePrisoner(5,2,2))