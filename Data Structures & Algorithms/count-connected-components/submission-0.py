class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False]*n

        def dfs(node,prev):
            if visited[node]:
                return
            visited[node] = True
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                dfs(neighbor,node)

        comps = 0
        for i in range(n):
            if visited[i]:
                continue
            dfs(i,-1)
            comps += 1
        
        return comps