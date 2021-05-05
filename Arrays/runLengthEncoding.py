
"""

["a", "a", "c", "c", "c", "b"] -> 2a3c1b
["a","a", "a", "a, "d", "d","a"] -> 4a2d1a

["c","c",", "c", "c", "c"] -> 5c
["a", "b", "c", "d"] - > 1a1b1c1d


answer string - "4a" 
Go through the loop. Have a character and a counter variable.

Time Complexity - O(N)
Space Complexity - O(k), where k is less than N


"""

def run_length(arr): 
    answer = ""
    char = ""
    counter = 0
    
    for i in range(len(arr)):
        
        
        if i == 0:
            char = arr[i]
            counter = 1
        
        elif arr[i] == arr[i - 1]:
            counter += 1
            
            if i == len(arr) - 1:
                answer+=str(counter)
                answer+=char
            
        else:
            answer+= str(counter)
            answer+=char
            
            char = arr[i]
            counter = 1
            
            if i == len(arr) - 1:
                answer+=str(counter)
                answer+=char
    return answer

print(run_length(["c", "c", "c", "c", "c", "c"]))