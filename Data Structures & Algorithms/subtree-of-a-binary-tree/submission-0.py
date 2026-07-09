# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(s, t):
            if not s and not t:
                return True
            if not s and t or not t and s:
                return False

            return s.val == t.val and same(s.right, t.right) and same(s.left, t.left)


        if same(root, subRoot) or not subRoot:
            return True
        if not root:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)