# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(node: Optional[TreeNode]) -> int:
            """returns the height of the binary tree,
            or -1 if the tree is unbalanced"""
            if not node:
                return 0
            
            left_height = check(node.left)
            if left_height == -1:
                return -1
            
            right_height = check(node.right)
            if right_height == -1:
                return -1

            if abs(right_height - left_height) > 1:
                return -1
            
            return 1 + max(right_height, left_height)
        
        return check(root) != -1

