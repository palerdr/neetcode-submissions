"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        

        q = deque([node])
        clone_root = Node(val=node.val)
        store = {
            node : clone_root
        }

        while q:
            #visiting a node means creating a clone and processing all neighbors
            cur_node = q.popleft()

            clone_node = store[cur_node]

            for nei_node in cur_node.neighbors:
                
                if nei_node not in store:
                    store[nei_node] = Node(val=nei_node.val)
                    q.append(nei_node)
                
                nei_clone = store[nei_node]

                clone_node.neighbors.append(nei_clone)

                    

        return clone_root
