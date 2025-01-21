"""
Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.
"""


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        topSum = sum(grid[0])
        bottomSum = 0
        ans =[]
        for i in range(len(grid[0])):
            topSum -= grid[0][i]
            ans.append(max(topSum,bottomSum))
            bottomSum += grid[1][i]

        return min(ans)