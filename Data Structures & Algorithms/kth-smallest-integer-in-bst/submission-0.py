# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        #leverage structure of BST, in order traversal will yield a sorted list, 1-indexed to kth from left

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

            return
        dfs(root)
        return res[k-1]