class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        def dfs(r,c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
                
                if r-1 >= 0:
                    dfs(r-1,c)
                if c-1 >= 0:
                    dfs(r,c-1)
                if r+1 < m:
                    dfs(r+1,c)
                if c+1 < n:
                    dfs(r,c+1)
        
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] =="1":
                    cnt +=1
                    dfs(r,c)
                else:
                    pass
        
        return cnt
                
                