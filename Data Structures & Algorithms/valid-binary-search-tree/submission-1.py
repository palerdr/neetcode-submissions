# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = 10**18

        def dfs(node, l ,r):
            if not node:
                return True
            
            if node.left and not (l < node.left.val < node.val):
                return False
            if node.right and not (node.val < node.right.val < r):
                return False
            
            return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
        

        return dfs(root, -INF, INF)
                
            