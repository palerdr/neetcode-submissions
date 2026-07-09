class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src,dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        #now when we pop the next node is the lexographically smallest

        path = []
        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            path.append(airport)
        dfs("JFK")
        #only add on the way back so only starts our path when we find a valid itinerary

        return path[::-1]