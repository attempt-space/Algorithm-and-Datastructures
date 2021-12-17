#Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 4

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        column = len(matrix[0])
        sum = 0
        for i in range(row):
            for j in range(column):
                matrix[i][j] = int(matrix[i][j])
        for i in range(1,row):
            for j in range(1,column):
                if int(matrix[i][j]) ==1:
                    matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]),int(matrix[i-1][j-1]))+1

        max_ = -1
        for i in range(row):
            max_ = max(max_,max(matrix[i]))
                    
        return max_**2
                