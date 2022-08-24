from typing import List


class Solution:

    def hanotaCore(self, size: int, A: List[int], B: List[int], C: List[int]) -> None:
        # base case
        # put one last small plate on top of C
        if size == 1:
            C.append(A.pop())
            return
        # put n-1 plates to B, so biggest plate can be placed to C
        self.hanotaCore(size - 1, A, C, B)
        # put biggest plate to C
        C.append(A.pop())
        # put n-1 plates on B back to C and finish it
        self.hanotaCore(size - 1, B, A, C)

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        if not A:
            return
        self.hanotaCore(len(A), A, B, C)
