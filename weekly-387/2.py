"""
3070. Count Submatrices with Top-Left Element and Sum Less Than k
User Accepted:10330
User Tried:12269
Total Accepted:10751
Total Submissions:20161
Difficulty:Medium
You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

 

Example 1:


Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.


"""

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        row, col = len(grid), len(grid[0])
        dp = [[0 for i in range(col + 1)] for j in range(row + 1)]
        for r in range(row):
            curr_sum = 0
            for c in range(col):
                curr_sum += grid[r][c]
                dp[r+1][c+1] = curr_sum + dp[r][c+1]
         
        
        def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
            return dp[row2 + 1][col2 + 1] + dp[row1][col1] - dp[row1][col2 + 1] - dp[row2 + 1][col1]  

        count = 0
        for r in range(row):
            for c in range(col):
                area = sumRegion(0, 0, r, c)
                if area <= k:
                    count += 1
        return count 