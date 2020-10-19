def revString(s):
    L = list(s)

    i = 0 
    j= len(L) - 1

    while i < j:
        L[i], L[j] = L[j], L[i]

        i += 1
        j -= 1
    
    return("".join(L))


print(revString("Hello"))