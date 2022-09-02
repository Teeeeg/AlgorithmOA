from typing import List


class Solution:

    def judgePoint24Core(self, cards: List[int]):
        n = len(cards)
        if n == 1:
            return abs(cards[0] - 24) < 1e-9

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                num1 = cards[i]
                num2 = cards[j]

                newCards = [cards[k] for k in range(n) if k != i and k != j]
                # newCards + [num1 + num2] won't append to original
                if self.judgePoint24Core(newCards + [num1 + num2]):
                    return True
                if self.judgePoint24Core(newCards + [num1 - num2]):
                    return True
                if self.judgePoint24Core(newCards + [num1 * num2]):
                    return True

                if num2 == 0:
                    continue
                if self.judgePoint24Core(newCards + [num1 / num2]):  # type: ignore
                    return True

        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        return self.judgePoint24Core(cards)


cards = [1, 3, 4, 6]
slt = Solution()
print(slt.judgePoint24(cards))