class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s2)
        m = len(s1)
        counter1 = {}
        counter2 = {}
        left = 0
        count = 0

        for ch in s1:
            counter1[ch] = counter1.get(ch, 0) + 1

        for right in range(n):
            rightChr = s2[right]
            counter2[rightChr] = counter2.get(rightChr, 0) + 1
            # 当右字符达标的时候+1
            if rightChr in counter1 and counter2[rightChr] == counter1[rightChr]:
                count += 1
                if count == len(counter1):
                    return True

            if right - left + 1 >= m:
                leftChr = s2[left]
                # 当左字符从达标的时候出去时 -1
                if leftChr in counter1 and counter2[leftChr] == counter1[leftChr]:
                    count -= 1
                counter2[leftChr] -= 1
                left += 1

        return False


s1 = "trinit"
s2 = "dinitrophenylhydrazinetrinit"
slt = Solution()
print(slt.checkInclusion(s1, s2))