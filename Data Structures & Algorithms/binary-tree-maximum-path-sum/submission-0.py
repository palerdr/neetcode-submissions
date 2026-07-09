# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = root.val

        def dfs(node):
            nonlocal global_max
            if not node:
                return 0
            left_down = max(dfs(node.left),0)
            right_down = max(dfs(node.right),0)

            max_through_path = node.val + left_down + right_down
            global_max = max(global_max, max_through_path)

            max_downward_path = node.val + max(left_down, right_down)
            return max_downward_path
        #returns max downward path but updates global with max through entire tree thus far
        dfs(root)
        return global_max

            
