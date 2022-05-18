class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        st = set()
        left = 0
        res = 0

        for right in range(n):
            while s[right] in st:
                st.remove(s[left])
                left += 1
            st.add(s[right])
            res = max(res, len(st))

        return res


s = "bbbbb"
slt = Solution()
print(slt.lengthOfLongestSubstring(s))