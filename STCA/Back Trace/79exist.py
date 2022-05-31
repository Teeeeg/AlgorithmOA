from typing import List


class Solution:
    # 回溯，在回溯开始判断
    def bfs(self, board: List[List[str]], word: str, index: int, cur, visited):
        # 因为是在回溯开始时判断，所以True是 n 的时候
        if index == len(word):
            return True

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 一开始应该添加
        visited.add(cur)
        for dir in dirs:
            nextDir = (cur[0] + dir[0], cur[1] + dir[1])
            # 不越界
            if 0 <= nextDir[0] < len(board) and 0 <= nextDir[1] < len(board[0]) and nextDir not in visited:
                # 回溯开始时
                if word[index] == board[nextDir[0]][nextDir[1]]:
                    # 若有就立刻返回
                    if self.bfs(board, word, index + 1, nextDir, visited):
                        return True
        # 回溯
        visited.remove(cur)

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) * len(board[0]) < len(word):
            return False

        visited = set()
        # 找到入口点
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    cur = (i, j)
                    if self.bfs(board, word, 1, cur, visited):
                        return True

        return False


board = board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

slt = Solution()
print(slt.exist(board, word))
