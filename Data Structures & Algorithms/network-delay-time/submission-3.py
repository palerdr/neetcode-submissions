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

            for ntime,n in adj[curr]:
                t = ntime + ctime
                if t < best[n]:
                    best[n] = t
                    heapq.heappush(q, (t,n))
        #finds the minimum, we need the largest because all nodes must get signal

        for num in best[1:]:
            if num == INF:
                return -1

        return max(best[1:])

        

