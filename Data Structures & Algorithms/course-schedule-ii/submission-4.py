class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        taken = defaultdict(int)
        courses = []

        def dfs(c):
            if c not in adj:
                courses.append(c)
                taken[c] = 2
                return True

            if taken[c] == 1:
                return False

            taken[c] = 1
            for n in adj[c]:
                if n in courses:
                    continue
                if not dfs(n):
                    return False
            courses.append(c)
            taken[c] = 2
            return True
        
        for i in range(numCourses):
            if taken[i] != 2:
                if not dfs(i):
                    return []

        return courses 