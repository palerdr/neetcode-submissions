# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = []
        
        q = []
        q.append((0,root))

        def bfs(r):
            l=-1
            while q:
                level, c = q.pop(0)
                if level>l:
                    ret.append(c.val)
                    l=level
                if c.right:
                    q.append((level+1, c.right))
                if c.left:
                    q.append((level+1, c.left))
        bfs(root)

        return ret
        
