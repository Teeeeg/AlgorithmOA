class Solution:

    def judgeCircle(self, moves: str) -> bool:
        dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        step = [0, 0]

        for ch in moves:
            dir = dirs[ch]
            step = [step[0] + dir[0], step[1] + dir[1]]

        return step == [0, 0]


moves = "UD"
slt = Solution()
print(slt.judgeCircle(moves))