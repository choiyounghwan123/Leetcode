# 463. Island Perimeter

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if 0 <= i-1 < len(grid) and grid[i-1][j]:
                        perimeter -= 1
                    if 0 <= i+1 < len(grid) and grid[i+1][j]:
                        perimeter -= 1
                    if 0<= j-1 < len(grid[i]) and grid[i][j-1]:
                        perimeter -=1
                    if 0 <= j+1 < len(grid[i]) and grid[i][j+1]:
                        perimeter -= 1
        return perimeter

solution = Solution()
print(solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))