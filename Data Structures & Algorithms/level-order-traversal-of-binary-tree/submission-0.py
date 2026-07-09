# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        ret = []
        q.append(root)

        while q:
            ql = len(q) #tells us how many in this level
            temp = []
            for i in range(ql):
                curr = q.popleft()
                if curr:
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if temp:
                ret.append(temp)

        return ret
