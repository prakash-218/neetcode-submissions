class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = {}
        n = len(grid)
        m = len(grid[0])
        count = 0
        for row in range(n):
            for col in range(m):
                if f'{row}_{col}' in vis:
                    continue
                
                if grid[row][col] == "0":
                    continue
                
                q = [[row, col]]
                count += 1
                while q:
                    r, c = q.pop()
                    if 0 <= r < n and 0 <= c < m and f'{r}_{c}' not in vis and grid[r][c] == "1":
                        vis[f'{r}_{c}'] = 1
                        q.extend([[r-1, c], [r, c-1], [r+1,c], [r, c+1]])
        return count