"""

3071. Minimum Operations to Write the Letter Y on a Grid
User Accepted:6031
User Tried:7128
Total Accepted:6243
Total Submissions:10486
Difficulty:Medium
You are given a 0-indexed n x n grid where n is odd, and grid[r][c] is 0, 1, or 2.

We say that a cell belongs to the Letter Y if it belongs to one of the following:

The diagonal starting at the top-left cell and ending at the center cell of the grid.
The diagonal starting at the top-right cell and ending at the center cell of the grid.
The vertical line starting at the center cell and ending at the bottom border of the grid.
The Letter Y is written on the grid if and only if:

All values at cells belonging to the Y are equal.
All values at cells not belonging to the Y are equal.
The values at cells belonging to the Y are different from the values at cells not belonging to the Y.
Return the minimum number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to 0, 1, or 2.

 

Example 1:


Input: grid = [[1,2,2],[1,1,0],[0,1,0]]
Output: 3
Explanation: We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 1 while those that do not belong to Y are equal to 0.
It can be shown that 3 is the minimum number of operations needed to write Y on the grid.

"""

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        ans = float("inf")
        
                
        inner0 = 0
        inner1 = 0
        inner2 = 0
        
        r, c = len(grid) // 2, len(grid) // 2
        visited = set()
        visited.add((r,c))
        tr, tc = r, c
        
        if grid[tr][tc] != 0:
            inner0 += 1
        if grid[tr][tc] != 1:
            inner1 += 1
        if grid[tr][tc] != 2:
            inner2 += 1
         
        
        # down
        while 0 <= tr + 1 and tr + 1 < len(grid) and 0 <= tc and tc < len(grid):
            tr = tr + 1
            tc = tc 
            visited.add((tr,tc))
            if grid[tr][tc] != 0:
                inner0 += 1
            if grid[tr][tc] != 1:
                inner1 += 1
            if grid[tr][tc] != 2:
                inner2 += 1
         
        tr, tc = r, c 
        while 0 <= tr - 1 and tr - 1 < len(grid) and 0 <= tc - 1 and tc - 1 < len(grid):
            tr = tr - 1
            tc = tc - 1
            visited.add((tr,tc))
            if grid[tr][tc] != 0:
                inner0 += 1
            if grid[tr][tc] != 1:
                inner1 += 1
            if grid[tr][tc] != 2:
                inner2 += 1
                 
        tr, tc = r, c 
        while 0 <= tr - 1 and tr - 1 < len(grid) and 0 <= tc + 1 and tc + 1 < len(grid):
            tr = tr - 1
            tc = tc + 1
            visited.add((tr,tc))
            if grid[tr][tc] != 0:
                inner0 += 1
            if grid[tr][tc] != 1:
                inner1 += 1
            if grid[tr][tc] != 2:
                inner2 += 1
          
        outer0 = 0
        outer1 = 0
        outer2 = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if (i, j) not in visited:
                    if grid[i][j] != 0:
                        outer0 += 1
                    if grid[i][j] != 1:
                        outer1 += 1
                    if grid[i][j] != 2:
                        outer2 += 1
        
       

        ans = min(ans, inner0 + outer1)
        ans = min(ans, inner0 + outer2)
        ans = min(ans, inner1 + outer0)
        ans = min(ans, inner1 + outer2)
        ans = min(ans, inner2 + outer1)
        ans = min(ans, inner2 + outer0)
        return ans 
    