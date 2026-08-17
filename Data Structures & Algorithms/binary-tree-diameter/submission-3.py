# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_diameter = 0
        # when you calculate the height of a subtree
        # you will be forced to traverse the whole depth
        # so at every level you get the diameter and only process each once
        def height(root: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not root:
                return 0
            else:
                left_height = height(root.left)
                right_height = height(root.right)
                candidate_diameter = left_height + right_height
                max_diameter = max(max_diameter, candidate_diameter)

                return 1 + max(left_height, right_height)
        
        height(root)
        return max_diameter

