#  https://leetcode.com/problems/robot-return-to-origin/

import time
start = time.time()

# def judgeCircle(moves):
#     """
#     :type moves: str
#     :rtype: bool
#     """
#     if (moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")):
#         return True
#     else:
#         return False

# print(judgeCircle("UD"))

def judgeCircle(moves: str) -> bool:
    moveX = 0
    moveY = 0

    for i in moves:
        if i == 'U':
            moveY += 1
        elif i == 'D':
            moveY -= 1
        elif i == 'R':
            moveX += 1
        elif i == 'L':
            moveX -= 1
        else: 
            print('Error')

    if moveX == 0 and moveY == 0:
        return True
    else:
        return False

print(judgeCircle("UD"))

print("=============")
print(time.time() - start)