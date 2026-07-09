class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src,dest in tickets:
            adj[src].append(dest)
        for src in adj:
            adj[src].sort()
        
        traveled = defaultdict(int)
        for t in tickets:
            traveled[tuple(t)] += 1
        

        path = ["JFK"]

        def dfs(airport):
            if len(path) == len(tickets) + 1:
                return True

            for neighbor in adj[airport]:
                ticket = (airport,neighbor)
                if traveled[ticket] == 0:
                    continue
                traveled[ticket] -= 1
                path.append(neighbor)
                if dfs(neighbor):
                    return True
                path.pop()
                traveled[ticket] += 1
            
            return False
            
        dfs("JFK")  

        return path

    