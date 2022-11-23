from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rowSet = set()
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue

                if num in rowSet:
                    return False

                rowSet.add(num)

        for col in range(9):
            colSet = set()
            for row in range(9):
                num = board[row][col]
                if num == '.':
                    continue

                if num in colSet:
                    return False

                colSet.add(num)

        id2Set = {i: set() for i in range(9)}

        for row in range(9):
            for col in range(9):
                blockId = row // 3 * 3 + col // 3
                num = board[row][col]
                if num == '.':
                    continue

                if num in id2Set[blockId]:
                    return False

                id2Set[blockId].add(num)

        return True


board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

slt = Solution()
print(slt.isValidSudoku(board))