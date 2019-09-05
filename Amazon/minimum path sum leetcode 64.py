# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

#Leetcode 64class Solution:
def minPathSum(grid: List[List[int]]) -> int:
    #把第一个数和第一列第一行写if；取min
    if grid is None or len(grid) == 0:
        return 0
    m = len(grid)
    n = len(grid[0])
    # paths = [[grid[0][0] for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[m-1][n-1]

def main():
    grid = [[0,0],[9,3]]
    minPathSum(grid)