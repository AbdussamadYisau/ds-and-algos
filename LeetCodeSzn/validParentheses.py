class Solution:
    def isValid(self, s: str) -> bool: 
        stack = []
        bracketsHashmap = {')': '(', ']':'[', '}':'{'}
        
        
        for c in s:
            if c in bracketsHashmap: 
                if stack and stack[-1] == bracketsHashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False
#     def isValidBrute(self, s: str) -> bool:
#         circleArray = []
#         parenthesesArray = []
#         boxArray = []
        
#         parenthesesHashmap = {}
        
# #       Populate Hashmap

#         for i in s: 
#             if i in parenthesesHashmap:
#                 parenthesesHashmap[i] += 1
            
#             else: 
#                 parenthesesHashmap[i] = 1
        
#         for i in s:
#             if i == '(' or i == ')':
#                 circleArray.append(i)
#             if i == '[' or i == ']':
#                 boxArray.append(i)
#             if i == '{' or i == '}':
#                 parenthesesArray.append(i)
                
        
#         # if len(circleArray)%2 == 0 and len(parenthesesArray)%2 == 0 and len(boxArray)%2 == 0 and (parenthesesHashmap['('] == parenthesesHashmap[')']) and (parenthesesHashmap['['] == parenthesesHashmap[']']) and (parenthesesHashmap['{'] == parenthesesHashmap['}']):
#         #     return true
#         if len(circleArray)%2 == 0 and (parenthesesHashmap['('] == parenthesesHashmap[')']):
#             return True
#         return False
        
    
                
                
        