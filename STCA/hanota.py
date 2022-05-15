from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        self.hanotaCore(n, A, B, C)

    def hanotaCore(self, n, A: List[int], B: List[int], C: List[int]):
        if n == 1:
            C.append(A.pop())
            return

        self.hanotaCore(n - 1, A, C, B)
        C.append(A.pop())
        self.hanotaCore(n - 1, B, A, C)


A = [2, 1, 0]
B = []
C = []
slt = Solution()
slt.hanota(A, B, C)
print(C)
