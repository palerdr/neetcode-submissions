class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 10**18
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((t,v))

        q = []
        best = [INF]*(n+1)
        heapq.heappush(q, (0,k))
        best[k] = 0

        while q:
            ctime,curr = heapq.heappop(q)
            if ctime != best[curr]:
                continue

            for ntime,neighbor in adj[curr]:
                newtime = ntime + ctime
                if newtime < best[neighbor]:
                    best[neighbor] = newtime
                    heapq.heappush(q, (newtime,neighbor))
        #finds the minimum, we need the largest because all nodes must get signal

        ret = max(best[1:])
        return ret if ret < INF else -1
        

