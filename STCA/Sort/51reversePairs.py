from typing import List


class Solution:
    # 利用归并排序

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        mid = n // 2

        leftPart = nums[:mid]
        rightPart = nums[mid:]
        res = 0

        # 统计分治之后的逆序数
        res += self.reversePairs(leftPart)
        res += self.reversePairs(rightPart)

        i = j = k = 0
        while i < len(leftPart) and j < len(rightPart):
            if leftPart[i] <= rightPart[j]:
                nums[k] = leftPart[i]
                i += 1
            else:
                nums[k] = rightPart[j]
                # 记录贡献
                # 当前 leftPart[i] > rightPart[j]
                # 说明 leftPart中[i: mid) 都比 rightPart[j] 大
                # 因此添加 mid - i
                res += mid - i
                j += 1
            k += 1

        while i < len(leftPart):
            nums[k] = leftPart[i]
            i += 1
            k += 1

        while j < len(rightPart):
            nums[k] = rightPart[j]
            j += 1
            k += 1

        return res


slt = Solution()
nums = [7, 10, 5, 6, 4]
print(slt.reversePairs(nums))