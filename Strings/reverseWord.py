'''
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello                      world!  "
sol= []
"hello        world!"
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

'''

def revWord(expr):
    
    n = len(expr)
    start = end = n -1
    out  = []
    while start >= 0:
        if expr[end] == ' ':
            end -= 1
             
        if expr[start] != ' ' and ((start-1) < 0 or expr[start-1] == ' '):
            out.append(expr[start:end+1])
            end = start - 1
        start -= 1
    return out
        

def revWordEasy(s): 
    s = s.strip()

    listWords = s.split()

    return " ".join([i for i in listWords[::-1] if i!=""])
    
print(revWord("the      sky is blue"))
    
    

        
    
        