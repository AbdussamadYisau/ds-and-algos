'''
PROBLEM STATEMENT: 

Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), 
square brackets: [],
and curly brackets: {}.
Assume that the string doesn’t contain any other character than these, 
no spaces words or numbers. As a reminder,
balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.

'''

def balanceCheck(expr):

	#Check for even number of brackets

	if len(expr)%2 != 0:
		return False

	# Make a set of opening brackets

	opening = set("([{")

	"Make a set of matching pairs"

	matches = set([("(",")"), ("{", "}"), ("[", "]")])

	# Use a list as a stack

	stack = []

	#Check every parenthesis in string 

	for paren in expr:

		if paren in opening:
			stack.append(paren)

		else:

			if len(stack) == 0:
				return False

			prevExpr = stack.pop()

			if (prevExpr,paren) not in matches:
				return False
	return len(stack) == 0

print(balanceCheck("[](){([[[]]])}"))



