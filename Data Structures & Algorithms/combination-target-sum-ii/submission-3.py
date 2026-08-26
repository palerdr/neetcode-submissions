class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = candidates
        n = len(c)
        r,t = [],[]
        c.sort()

        def dfs(i, s):
            if i > n:
                return
            
            if s > target:
                return
            
            if s == target:
                r.append(t[:])
                return
            
            for j in range(i, n):
                if s + c[j] > target:
                    break

                if j != i and c[j] == c[j-1]:
                    continue
                
                t.append(c[j])
                dfs(j+1, s + c[j])
                t.pop()
        dfs(0, 0)
        return r
        