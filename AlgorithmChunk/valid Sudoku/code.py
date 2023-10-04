class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        import collections
        for j in range(9):
            templist = {}
            for i in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in templist:
                    return False
                else:
                    templist[board[j][i]] =1
            # print(templist)
            for key,value in templist.items():
                if value >1:
                    return False
        for j in range(9):
            templist = {}
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in templist:
                    return False
                else:
                    templist[board[i][j]] =1
            # print(templist)
            for key,value in templist.items():
                if value >1:
                    return False
        templist = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in templist[(i//3,j//3)]:
                    return False
                else:
                    print(templist)
                    templist[(i//3,j//3)].add(board[i][j])
            
        return True