class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        INF = 10**18
        n = len(points)

        edges,ret,node = 0,0,0
        seen = [False]*n
        dist = [INF]*n 
        while edges < n-1:
            seen[node] = True
            x,y = points[node]
            for i in range(n):
                if not seen[i]:
                    cost = abs(x-points[i][0]) + abs(y-points[i][1])
                    dist[i] = min(dist[i], cost)
            nxt = min(
                (i for i in range(n) if not seen[i]), 
                key=lambda i: dist[i]
            )
            ret += dist[nxt]
            node = nxt
            edges += 1
        
        return ret

