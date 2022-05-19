class Solution:

    def reverseWords(self, s: str) -> str:
        sList = [word for word in s.split(' ') if len(word) > 0]
        return ' '.join(sList[::-1])


class Solution1:

    def trim(self, s):
        n = len(s)
        left, right = 0, n - 1

        # 去除左右的空格
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        res = []
        # 去除中间多余的空格
        while left <= right:
            # 若left不是空格，则添加
            if s[left] != ' ':
                res.append(s[left])
            # 遇到空格了，但是是一个不是空格，该空格有效
            elif res[-1] != ' ':
                res.append(s[left])
            # 该空格无效，left继续向后
            left += 1

        return res

    def reverseArray(self, arr, left, right):
        # 根据left，right翻转
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def reverseWord(self, arr):
        slow, fast = 0, 0
        n = len(arr)
        # 实现每个单词的翻转
        # 即要越过空格
        while slow < n:
            # fast一直访问到空格位置
            while fast < n and arr[fast] != ' ':
                fast += 1
            # 此时[slow, fast-1]为一个单词
            self.reverseArray(arr, slow, fast - 1)
            # 跳转下一个单词
            slow = fast + 1
            fast += 1

    def reverseWords(self, s: str) -> str:
        sList = self.trim(s)
        self.reverseArray(sList, 0, len(sList) - 1)
        self.reverseWord(sList)
        return ''.join(sList)


s = "the sky is blue"
slt = Solution1()
print(slt.reverseWords(s))