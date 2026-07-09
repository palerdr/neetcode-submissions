class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        adj = defaultdict(list)
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        taken = defaultdict(int)

        def dfs(c):
            if c not in adj:
                return True
            if taken[c] == 1:
                return False

            taken[c] = 1
            for p in adj[c]:
                if not dfs(p):
                    return False
            taken[c] = 2
            return True
        
        for pre in prerequisites:
            if not dfs(pre[0]):
                return False
        return True

