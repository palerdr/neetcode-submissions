class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image) - 1
        m = len(image[0]) - 1

        def dfs(i,j,c):
            if i > n or j > m or i < 0 or j < 0:
                return
            elif image[i][j] != c or image[i][j] == color:
                return
            else:
                image[i][j] = color
                neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                for (n1,n2) in neighbors:
                    dfs(n1,n2,c)
        
        dfs(sr, sc, image[sr][sc])
        return image