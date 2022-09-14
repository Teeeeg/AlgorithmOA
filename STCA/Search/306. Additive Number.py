class Solution:

    def isValid(self, num: str):
        if len(num) > 1 and num[0] == '0' or not num:
            return False

        return True

    def isAdditiveNumberCore(self, num: str, preNum1, preNum2, index):

        if not self.isValid(num[index:]):
            return False

        curNum = int(num[index:])
        if curNum == preNum1 + preNum2:
            return True

        for i in range(index, len(num)):
            if not self.isValid(num[index:i + 1]):
                continue

            curNum = int(num[index:i + 1])
            if curNum != preNum1 + preNum2 or curNum == 0:
                continue
            if self.isAdditiveNumberCore(num, preNum2, curNum, i + 1):
                return True

        return False

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i):
                if not self.isValid(num[:j + 1]) or not self.isValid(num[j + 1:i + 1]):
                    continue
                preNum1 = int(num[:j + 1])
                preNum2 = int(num[j + 1:i + 1])

                if self.isAdditiveNumberCore(num, preNum1, preNum2, i + 1):
                    return True

        return False


num = "199100199"
slt = Solution()
print(slt.isAdditiveNumber(num))