class Solution:

    def makeLargestSpecial(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return ''
        # substring start index
        start = 0
        # remember 1 and 0 difference
        diff = 0
        strs = []
        for i in range(n):
            if s[i] == '1':
                diff += 1
            else:
                diff -= 1

            # if diff == 0, recursively check its substring
            if diff == 0:
                # strip outlier 0 and 1
                sub = self.makeLargestSpecial(s[start + 1:i])
                # put back 0 and 1
                strs.append('1' + sub + '0')
                # update the new start
                start = i + 1
        # sort with string
        strs.sort(reverse=True)

        return ''.join(strs)


s = "101011001110011010001111100000"
slt = Solution()
print(slt.makeLargestSpecial(s))