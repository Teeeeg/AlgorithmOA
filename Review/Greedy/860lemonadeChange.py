from typing import List


class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = [0] * 2

        for bill in bills:
            if bill == 5:
                counts[0] += 1

            elif bill == 10:
                if counts[0]:
                    counts[0] -= 1
                else:
                    return False
                counts[1] += 1

            elif bill == 20:
                if counts[1] and counts[0]:
                    counts[1] -= 1
                    counts[0] -= 1
                elif counts[0] >= 3:
                    counts[0] -= 3
                else:
                    return False

        return True


bills = [5, 5, 5, 5, 10, 5, 10, 10, 10, 20]
slt = Solution()
print(slt.lemonadeChange(bills))