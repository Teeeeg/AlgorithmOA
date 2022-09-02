class Solution:

    def isValid(self, num1: int, num2: int, used):
        # 2 -> 9 or adjacent
        if (num1 + num2) % 2 == 1:
            return True

        mid = (num1 + num2) // 2
        # cross 5
        if mid == 5:
            return used[5]

        if ((num1 - 1) % 3 != (num2 - 1) % 3) and ((num1 - 1) // 3 != (num2 - 1) // 3):
            return True
        # others 1 -> 3
        return used[mid]

    def numberOfPatternsCore(self, num1: int, countLeft: int, used):
        if countLeft == 0:
            return 1

        total = 0
        for num2 in range(1, 10):
            if used[num2] or not self.isValid(num1, num2, used):
                continue
            used[num2] = True
            total += self.numberOfPatternsCore(num2, countLeft - 1, used)
            used[num2] = False

        return total

    def numberOfPatterns(self, m: int, n: int) -> int:
        res = 0
        used = [False] * 10

        for countLeft in range(m, n + 1):
            for num1 in range(1, 10):
                used[num1] = True
                res += self.numberOfPatternsCore(num1, countLeft - 1, used)
                used[num1] = False

        return res


m = 1
n = 3
slt = Solution()
print(slt.numberOfPatterns(m, n))