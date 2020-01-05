# These are the questions I was asked on Goldman Sach's tes (2020)


# 1 - First Unique Char
from collections import defaultdict
def firstUniqueChar(s):
    for i in s.lower():
        if s.lower().count(i) == 1 and i != " ":
            return i
print(firstUniqueChar("geeksforgeeks"))

# 2 - RunLength Encoding. Only 2/10 test cases ran succesfully here, so i switched to JS


from collections import OrderedDict 
def Encoding(expr): 
  
    # Generate ordered dictionary of all lower 
    # case alphabets, its output will be  
    # dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0} 
    dict=OrderedDict.fromkeys(expr, 0) 
  
    # Now iterate through input string to calculate  
    # frequency of each character, its output will be  
    # dict = {'w':4,'a':3,'d':1,'e':1,'x':6} 
    for ch in expr: 
        dict[ch] += 1
  
    # now iterate through dictionary to make  
    # output string from (key,value) pairs 
    output = '' 
    for key,value in dict.items(): 
         output = output + key + str(value) 
    return output 


# JS solution

# function encode(string) {
#     let count = 0;
#     let ans = "";
#     for (let i = 0; i < string.length; i++) {
#         count++;
#         if (!(i<string.length - 1 && string[i] === string[i+1])) {
#             ans += count + string[i]
#             count = 0
#         }
#     }
#     return ans
# }

