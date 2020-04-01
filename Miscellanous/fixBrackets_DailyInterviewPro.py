def fixBrackets(s):
  """
  Given a string with only ( and ), find the minimum number of characters to add or subtract to fix the string such that the brackets are balanced.

  Input: " (()()"
  Output: 1

  """
  leftBrack = []
  rightBrack = []
  for ele in range(0, len(s)):
    if s[ele] == "(":
      leftBrack += s[ele]
    else:
      rightBrack += s[ele]

  #print(leftBrack)
  #print(rightBrack)

  if(len(leftBrack) > len(rightBrack)):
    answer = len(leftBrack) - len(rightBrack)
    return(answer)

  elif(len(rightBrack) > len(leftBrack)):
    answer = len(rightBrack) - len(leftBrack)
    return(answer)
  else:
    return("Problem dey")



print(fixBrackets("(()())(("))
print(fixBrackets("(()()"))
