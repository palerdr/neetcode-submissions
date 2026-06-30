from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 10 slots 0-9 for 4 circular wheels
        # wrap around, so 4 number combination 4^10 combos
        # lock starts at 0000
        # deadends are sinks/dead states -> unable to open


        target = tuple(int(x) for x in target)
        deads = {tuple(int(x) for x in deadend) for deadend in deadends}

        start = (0,0,0,0)
        q = deque([(start, 0)])

        if start in deads:
            return -1
        deads.add(start)

        
        def wrap_up(x):
            if x == 9:
                return 0
            else:
                return x + 1
        def wrap_down(x):
            if x == 0:
                return 9
            else:
                return x-1

        while q:
            ((x1,x2,x3,x4), turns) = q.popleft()
            curr = (x1,x2,x3,x4)
            
            if curr == target:
                return turns

            neighbors = [
                (wrap_up(x1),x2,x3,x4),
                (wrap_down(x1),x2,x3,x4),
                (x1,wrap_up(x2),x3,x4),
                (x1,wrap_down(x2),x3,x4),
                (x1,x2,wrap_up(x3),x4),
                (x1,x2,wrap_down(x3),x4),
                (x1,x2,x3,wrap_up(x4)),
                (x1,x2,x3,wrap_down(x4)),
            ]

            for neighbor in neighbors:
                if neighbor in deads:
                    continue
                q.append((neighbor, turns + 1))
                deads.add(neighbor)
        

        return -1


            
