class Solution:

    def isAllWildCard(self, ptrn: str):
        for ch in ptrn:
            if ch != '*':
                return False

        return True

    def isCharMatch(self, src: str, ptrn: str, sIndex: int, pIndex: int):
        if src[sIndex] == ptrn[pIndex] or ptrn[pIndex] == '?':
            return True

        return False

    def isMatchCore(self, src: str, ptrn: str, sIndex: int, pIndex: int, memo):
        if pIndex == len(ptrn):
            return sIndex == len(src)

        if sIndex == len(src):
            return self.isAllWildCard(ptrn[pIndex:])

        if memo[sIndex][pIndex] != -1:
            return memo[sIndex][pIndex]

        if ptrn[pIndex] == '*':
            # if pattern is '*', it can divide into two ignore or not not igore
            memo[sIndex][pIndex] = self.isMatchCore(src, ptrn, sIndex + 1, pIndex, memo) or self.isMatchCore(src, ptrn, sIndex, pIndex + 1, memo)

            # much more easy way, iterate all possible match
            # for i in range(sIndex, len(src) + 1):
            #     if self.isMatchCore(src, ptrn, i, pIndex + 1, memo):
            #         memo[sIndex][pIndex] = True
            #         break
            # else:
            #     memo[sIndex][pIndex] = False
        else:
            memo[sIndex][pIndex] = self.isCharMatch(src, ptrn, sIndex, pIndex) and self.isMatchCore(src, ptrn, sIndex + 1, pIndex + 1, memo)

        return memo[sIndex][pIndex]

    def isMatch(self, s: str, p: str) -> bool:
        memo = [[-1] * len(p) for _ in range(len(s))]

        return self.isMatchCore(s, p, 0, 0, memo)


s = "adceb"
p = "*a*b"
slt = Solution()
print(slt.isMatch(s, p))