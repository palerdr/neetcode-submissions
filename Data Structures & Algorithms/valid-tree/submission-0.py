class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        #build adjacency list
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        v = [False]*n

        def dfs(node,prev):
            if v[node]:
                return False
            v[node] = True
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor,node):
                    return False  
            return True
        
        if not dfs(0,-1):
            return False
        return all(v)
            