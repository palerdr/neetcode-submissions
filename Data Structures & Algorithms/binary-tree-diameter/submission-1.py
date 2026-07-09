# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def dfs(root):
            if not root:
                return 0
            lefth = dfs(root.left)
            righth = dfs(root.right)
            DTN = lefth + righth #diameter through this node
            self.maxD = max(self.maxD, DTN) #global max diameter

            return 1 + max(lefth, righth) #height of the subtree

        dfs(root)
        return self.maxD