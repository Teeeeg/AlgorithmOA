class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False

        n1 = len(name)
        n2 = len(typed)

        p1 = 0
        p2 = 0

        while p2 < n2:
            if p1 < n1 and name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            elif p2 > 0 and typed[p2] == typed[p2 - 1]:
                p2 += 1
            else:
                return False

        return p1 == n1


name = "alex"
typed = "aaleex"
slt = Solution()
print(slt.isLongPressedName(name, typed))