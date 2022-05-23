from typing import List


class Solution:
    # 公式
    # G(n) = n xor (n>>1)
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))

        return res

    # n = 0  -> [0]
    # n = 1  -> [0, 1]
    # n = 2  -> [00, 01, 11, 10]
    # n = 3  -> [000, 001, 011, 010, 110, 111, 101, 100]
    # 观察获取规律
    # 2的前两位有1复制并且补0，后两位插1后到序插入
    # 补0的时候值不变，主要考虑1的位置

    def grayCode1(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            # 获取当前有几个
            lastLength = len(res)
            # 到序遍历
            for j in range(lastLength - 1, -1, -1):
                # 1本身是第一位，到达i的时候应该是i位，因此只需右移i-1位置
                num = res[j] | 1 << (i - 1)
                res.append(num)

        return res


n = 2
slt = Solution()
print(slt.grayCode1(1))