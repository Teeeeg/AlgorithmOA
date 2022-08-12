import math


class Solution:

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n1 = len(a)
        n2 = len(b)

        leftBound = math.ceil(n2 / n1)
        rightBound = leftBound + 1

        aa = a * rightBound
        k = 131
        mod = 10**9 + 7
        bHash = 0

        for ch in b:
            digit = ord(ch) - ord('a') + 1
            bHash = (bHash * k + digit) % mod

        aaPrefixHash = [0] * (n1 * rightBound + 1)
        powerOfK = [1] + [0] * (n1 * rightBound)

        for i in range(n1 * rightBound):
            ch = aa[i]
            digit = ord(ch) - ord('a') + 1
            aaPrefixHash[i + 1] = (aaPrefixHash[i] * k + digit) % mod
            powerOfK[i + 1] = (powerOfK[i] * k) % mod

        calcHash = lambda l, r: (aaPrefixHash[r + 1] - aaPrefixHash[l] * powerOfK[r - l + 1] + mod) % mod

        left = 0
        for right in range(n1 * rightBound):
            if left >= n1:
                break
            if right - left + 1 >= n2:
                if calcHash(left, right) == bHash:
                    index = left + n2
                    return math.ceil(index / n1)
                left += 1

        return -1


# abcabcabc
a = "abc"
b = "cabcabca"
slt = Solution()
print(slt.repeatedStringMatch(a, b))