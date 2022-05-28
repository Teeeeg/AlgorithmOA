class Solution:
    # 贪心思路
    # 看当前值的左边的值
    # 若左边的值大则不保留，最大位越来越小
    # 若该数组位递增，则直接截取
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        tail = len(num) - k

        for val in num:
            # 若当前值比stack顶顶值小则pop
            while stack and stack[-1] > val and k > 0:
                stack.pop()
                k -= 1
            stack.append(val)

        # 如果最终有k多，说明需要截取

        res = ''.join(stack[:tail]).lstrip('0')

        return res if res else '0'


num = "1432219"
k = 3
slt = Solution()
print(slt.removeKdigits(num, k))