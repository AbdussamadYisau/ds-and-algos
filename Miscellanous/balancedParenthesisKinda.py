'''
https://www.hackerrank.com/challenges/balanced-brackets/problem

'''

def balanceCheckDaddy(arr):
    def balanceCheck(expr):

	#Check for even number of brackets

        if len(expr)%2 != 0:
            return ("NO")

        # Make a set of opening brackets

        opening = set("([{")

        # Make a set of matching pairs

        matches = set([("(",")"), ("{", "}"), ("[", "]")])

        # Use a list as a stack

        stack = []

        #Iterate through the string, checking every parenthesis 

        for paren in expr:

            if paren in opening:
                stack.append(paren)

            else:

                if len(stack) == 0:
                    return ("NO")

                prevExpr = stack.pop()

                if (prevExpr,paren) not in matches:
                    return ("NO")
       
        return("YES")


    solution = []
    for i in arr:
        solution.append(balanceCheck(i))
    
    return solution


print(balanceCheckDaddy(["[{}]", "[{]}"]))


# Hackerrank solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):

#Check for even number of brackets

    if len(s)%2 != 0:
        return "NO"

    # Make a set of opening brackets

    opening = set("([{")

    # Make a set of matching pairs

    matches = set([("(",")"), ("{", "}"), ("[", "]")])

    # Use a list as a stack

    stack = []

    #Iterate through the string, checking every parenthesis 

    for paren in s:

        if paren in opening:
            stack.append(paren)

        else:

            if len(stack) == 0:
                return "NO"

            prevExpr = stack.pop()

            if (prevExpr,paren) not in matches:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()




    

