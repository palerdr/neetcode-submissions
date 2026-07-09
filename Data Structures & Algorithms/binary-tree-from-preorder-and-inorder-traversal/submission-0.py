# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        loc = inorder.index(root.val)
        left_length = len(inorder[:loc])
        right_length = len(inorder[loc+1:])

        root.left = self.buildTree(preorder[1:left_length+1], inorder[:loc])
        root.right = self.buildTree(preorder[left_length+1:], inorder[loc+1:])


        return root





