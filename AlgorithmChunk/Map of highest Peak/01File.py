"""
Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.
"""
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R = len(isWater)
        C = len(isWater[0])
        height = [[-1] * C for _ in range(R)] 
        queue = deque()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for i in range(R):
            for j in range(C):
                if isWater[i][j] == 1:
                    height[i][j]= 0 
                    queue.append((i,j))
        while queue:
            x,y =  queue.popleft()
            for dir1 in directions:
                newdir1,newdir2 = x+dir1[0],y+dir1[1]
                if 0 <= newdir1 < R and 0 <= newdir2 <C and height[newdir1][newdir2] == -1:

                    height[newdir1][newdir2] = height[x][y]+1
                    queue.append((newdir1,newdir2))

        return height
                    

        