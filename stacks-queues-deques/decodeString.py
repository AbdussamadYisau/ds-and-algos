'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
if the character you are looking at is a left bracket. Yep.

'''
def encodedString(expr):
    # Put open parenthesis in a set
    opening = set("[")
    
        # Make a set of matching pair
    
    match = set([("[", "]")])
    
    
    #Number list
    
    number = set(0,1,2,3,4,5,6,7,8,9)
    
    #Char list
    
    char = set("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    

    #Use a list as a stack, this checks balanced parenthesis
    parenStack = []
    # Use list to store numbers
    intStack = []
    # Use list to store characters 
    charStack = []
    
    
    #Iterate through the string to check for parenthesis
    for paren in expr:
        if paren in number:
            intStack.append(paren)
        elif paren in char:
            charStack.append(paren)
            
        else:
            if paren in opening:
                parenStack.append(paren)
            else: 
                if len(parenStack) ==  0:
                    return False
                prevExpr = parenStack.pop()

                if (prevExpr,paren) in match:
                    parenStack.append((prevExpr,paren))
    return len(parenStack) == 0
    
    
    
    
