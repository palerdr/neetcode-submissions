# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        INF = 10**18
        def dfs(node, temp_max):
            if not node:
                return 0
            
            good_nodes = 0
            if node.val >= temp_max:
                temp_max = node.val
                good_nodes += 1

            return good_nodes + dfs(node.left, temp_max) + dfs(node.right, temp_max)
        
        return dfs(root, -INF)

