from typing import List


class Solution:

    def lexicalOrderCore(self, i, n, res):
        # base case
        # 可写可不写，因为for已经限定了递归深度
        if i > n:
            return

        res.append(i)
        # 获取左右边界
        left = i * 10
        # 注意用min
        right = min(left + 9, n)
        # 对其每个子节点进行先序遍历
        for child in range(left, right + 1):
            self.lexicalOrderCore(child, n, res)

    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        # 一开始从1-9开始
        # 题目中不含0
        for i in range(1, min(9, n) + 1):
            self.lexicalOrderCore(i, n, res)

        return res

    def lexicalOrder1(self, n: int) -> List[int]:
        res = []
        num = 1
        while len(res) < n:
            while num <= n:
                # 先序
                res.append(num)
                # 不断添加左节点
                num *= 10
            # 类似于里边的pop
            # num%10 == 9代表是最右边的节点
            while num % 10 == 9:
                num //= 10
            # 向右遍历
            num += 1

        return res


slt = Solution()
n = 13
print(slt.lexicalOrder1(n))
