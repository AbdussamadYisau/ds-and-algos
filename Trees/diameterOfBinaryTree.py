# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        
        def heightOfTree( root):
            if root is None:
                return 0
            else: 
                lDepth = heightOfTree(root.left)
                rDepth = heightOfTree(root.right)
                
                self.ans = max(self.ans, lDepth + rDepth)

                if lDepth > rDepth:
                    return lDepth + 1
                else:
                    return rDepth + 1
        heightOfTree(root)

        return(self.ans)
        
        