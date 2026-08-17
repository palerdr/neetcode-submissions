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
        
        def depth(root: Optional[TreeNode]) -> int:
            q = deque()
            if root:
                q.append(root)

            h = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                h += 1
            return  h
        
        return max(
            depth(root.left) + depth(root.right),
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )