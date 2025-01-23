"""
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

"""
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        Rcount =[]
        Ccount =[]
        Rcount = [sum(i) for i in grid]
        for i in range(len(grid[0])):
            tempcount=0
            for j in range(len(grid)):
                tempcount += grid[j][i]
            Ccount.append(tempcount)
        returnTotal =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1  and (Rcount[i] >1  or Ccount[j]>1):
                    returnTotal+=1
        return returnTotal