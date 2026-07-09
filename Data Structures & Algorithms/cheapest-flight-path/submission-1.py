import heapq
from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        outgoing = defaultdict(list)
        for s,d,c in flights:
            #adjacency list with weights for every airport
            outgoing[s].append((d,c))

        best = defaultdict(lambda: inf)
        #all have infinite distance at first
        best[(src,0)] = 0
        #this node at this amount of stops costs this much
        frontier = [(0,0,src)]
        #here is our priority queue
        while frontier:
            cost, stops, node = heapq.heappop(frontier)

            if cost != best[(node,stops)]:
                continue
            #uses up replaced heap entries because there is no updates in heapq

            if node == dst:
                return cost
            #the first time dst is popped then it has been settled by dijkstras invariant
            #thus this is by definition the shortest path

            if stops > k:
                continue
            #don't explore farther than k stops

            for n,w in outgoing[node]:
                td = cost + w
                ts = stops + 1
                
                if td < best[(n,ts)]:
                    best[(n,ts)] = td
                    heapq.heappush(frontier, (td,ts,n))

        return -1
                

            
            
