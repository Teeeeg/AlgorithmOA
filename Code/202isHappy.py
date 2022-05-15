class Solution:
    def getNext(self, num):
        res = 0
        while num > 0:
            div, mod = divmod(num, 10)
            res += mod**2
            num = div

        return res

    def isHappy(self, n: int) -> bool:
        st = set()

        num = n
        while num != 1 and num not in st:
            st.add(num)
            num = self.getNext(num)

        return True if num == 1 else False


slt = Solution()
print(slt.isHappy(19))
