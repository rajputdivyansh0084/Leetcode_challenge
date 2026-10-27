class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Fill the first row (can only come from the left)
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
            
        # Fill the first column (can only come from above)
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                
        # The bottom-right cell contains the minimum path sum
        return grid[m - 1][n - 1]
