# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import functools
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @functools.lru_cache()
        def helper(root):
            if not root:
                return 0
            if root and not root.left and not root.right:
                return root.val

            c1 = root.val
            c2 = 0
            if root.right:
                c1 += helper(root.right.right) + helper(root.right.left)
                c2 += helper(root.right)

            if root.left:
                c1 += helper(root.left.right) + helper(root.left.left)
                c2 += helper(root.left)

            return max(c1,c2)

        return helper(root)
