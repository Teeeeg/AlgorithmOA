class Solution:

    def maxRepOpt1(self, text: str) -> int:
        char2Count = {}
        for char in text:
            char2Count[char] = char2Count.get(char, 0) + 1

        window = {}
        left = 0
        res = 0

        for right in range(len(text)):
            window[text[right]] = window.get(text[right], 0) + 1

            while len(window) > 2 or (len(window) == 2 and 1 not in window.values()):
                window[text[left]] -= 1
                if window[text[left]] == 0:
                    del window[text[left]]
                left += 1

            if len(window) == 1:
                res = max(res, right - left + 1)
                continue

            keys = [key for key in window.keys()]
            if char2Count[keys[0]] - window[keys[0]] >= 1 and window[keys[1]] == 1:
                res = max(res, right - left + 1)
            if char2Count[keys[1]] - window[keys[1]] >= 1 and window[keys[0]] == 1:
                res = max(res, right - left + 1)

        return res


text = "aabbaba"
slt = Solution()
print(slt.maxRepOpt1(text))
