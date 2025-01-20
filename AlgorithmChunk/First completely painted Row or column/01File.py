"""Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
https://leetcode.com/problems/first-completely-painted-row-or-column/description/"""

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row,column = len(mat),len(mat[0])
        map_position = {}
        for r  in range(row):
            for c in range(column):
                map_position[mat[r][c]]=(r,c)

        print(map_position)
        rowFreq = [0] * row
        colFreq = [0] * column
        for eachindex in range(len(arr)):
            paintindex = map_position[arr[eachindex]]
            rowFreq[paintindex[0]]+=1
            colFreq[paintindex[1]]+=1

            if rowFreq[paintindex[0]] == column or colFreq[paintindex[1]] == row:
                return eachindex
