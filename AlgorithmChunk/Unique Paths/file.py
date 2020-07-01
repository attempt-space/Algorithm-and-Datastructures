"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        countofpaths = [[0 for x in range(n)] for y in range(m)]
        print(countofpaths)
        for i in range(m):
            print(i)
            countofpaths[i][0] = 1
            
        for j in range(n):
            countofpaths[0][j] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                countofpaths[i][j] = countofpaths[i-1][j]+ countofpaths[i][j-1]
        
        return countofpaths[m-1][n-1]


    
