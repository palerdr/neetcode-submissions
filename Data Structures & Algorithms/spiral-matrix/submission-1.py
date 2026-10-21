class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        ans = []
        tr, bl = [0, n-1], [m-1, 0]
        done = False

        def update(i,j):
            nonlocal done
            ans.append(matrix[i][j])
            done = (len(ans) == m*n)
        
        def lap(tr, bl):
            for j in range(bl[1], tr[1]+1):
                update(tr[0], j)
            if done:
                return
            tr[0] += 1
            for i in range(tr[0], bl[0]+1):
                update(i, tr[1])
            if done:
                return
            tr[1] -= 1
            for j in range(tr[1], bl[1]-1, -1):
                update(bl[0], j)
            if done:
                return
            bl[0] -= 1
            for i in range(bl[0], tr[0]-1, -1):
                update(i, bl[1])
            if done:
                return
            bl[1] += 1

        while not done:
            lap(tr, bl)
            
        return ans 