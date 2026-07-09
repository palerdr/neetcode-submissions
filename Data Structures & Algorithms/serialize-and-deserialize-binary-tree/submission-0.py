# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = collections.deque([root])
        ser = []

        while q:
            node = q.popleft()

            if node is None:
                ser.append("!")
                continue

            ser.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return ",".join(ser)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        tokens = data.split(",")
        if tokens[0] == "!":
            return None
        
        root = TreeNode(tokens[0])
        q = collections.deque([root])

        loc = 0
        while q:
            node = q.popleft()
            for i in range(2):
                if loc >= len(tokens)-1:
                    continue
                loc += 1
                child = tokens[loc]
                if child == "!":
                    continue
                if i == 0 :
                    node.left = TreeNode(int(child))
                    q.append(node.left)
                else:
                    node.right = TreeNode(int(child))
                    q.append(node.right)

        return root




















