from typing import List


class Solution:

    def rowAndCol(self, board: List[List[str]], isRow):
        for i in range(9):
            visited = set()
            for j in range(9):
                if isRow:
                    if board[i][j] != '.':
                        if board[i][j] in visited:
                            return False
                        visited.add(board[i][j])
                else:
                    if board[j][i] != '.':
                        if board[j][i] in visited:
                            return False
                        visited.add(board[j][i])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.rowAndCol(board, True) or not self.rowAndCol(board, False):
            return False

        for i in range(3):
            for j in range(3):
                startRow = i * 3
                startCol = j * 3
                visited = set()
                for a in range(startRow, startRow + 3):
                    for b in range(startCol, startCol + 3):
                        num = board[a][b]
                        if num != '.':
                            if num in visited:
                                return False
                            visited.add(num)

        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

slt = Solution()
print(slt.isValidSudoku(board))