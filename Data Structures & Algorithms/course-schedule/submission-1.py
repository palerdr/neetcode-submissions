class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 

        from collections import deque, defaultdict

        in_degs = [0] * numCourses
        edges = defaultdict(list)

        for edge in prerequisites:
            out_node = edge[1]
            in_node = edge[0]
            in_degs[in_node] += 1
            edges[out_node].append(in_node)
        
        q = deque(
            [i for i in range(numCourses) if in_degs[i] == 0]
        )

        while q:
            course = q.popleft()

            for neighbor in edges[course]:
                in_degs[neighbor] -= 1
                if in_degs[neighbor] == 0:
                    q.append(neighbor)
        
        return not any(in_degs)
