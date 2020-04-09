
def compress(S):
    s = 0
    numBackSpace = 0
    idx = len(S) - 1
        
    while idx >= 0:
        if S[idx] != "#":
            if numBackSpace == 0:
                s += ord(S[idx])
            else:
                numBackSpace -= 1
        else:
            numBackSpace += 1
                
        idx -= 1
    return s
def backspaceCompare(S: str, T: str):
    return compress(S) == compress(T)
        
        
print(backspaceCompare("ab#c", "ac"))