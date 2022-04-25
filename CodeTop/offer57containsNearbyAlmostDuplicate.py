from typing import List

from sortedcontainers import SortedList


class Solution:
    # O(nk)
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = set()
        left = 0

        for right, num in enumerate(nums):
            if num in window:
                return True

            for item in window:
                if abs(item-num) <= t:
                    return True

            window.add(num)

            if right >= k:
                window.remove(nums[left])
                left += 1

        return False

    def containsNearbyAlmostDuplicate1(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return False

        window = SortedList()
        left = 0

        for right, num in enumerate(nums):
            if num in window:
                return True

            index = window.bisect_left(num)
            # 没有的时候
            if len(window) == 0:
                window.add(num)
                continue
            # index返回均有效
            if 0 <= index < len(window):
                if abs(window[index-1]-num) <= t or abs(window[index]-num) <= t:
                    return True
            # 在最后添加，index越界
            if index == len(window):
                if abs(window[index-1]-num) <= t:
                    return True

            window.add(num)

            if right >= k:
                window.remove(nums[left])
                left += 1

        return False

    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}
        left = 0
        size = t+1

        for right, num in enumerate(nums):
            id = self.getBucketID(nums[right], size)
            if id in buckets:
                return True

            if id-1 in buckets and abs(buckets[id-1]-num) <= t:
                return True
            if id+1 in buckets and abs(buckets[id+1]-num) <= t:
                return True

            buckets[id] = num

            if right >= k:
                del buckets[self.getBucketID(nums[left], size)]
                left += 1

        return False

    def getBucketID(self, num, size):
        if num > 0:
            return num // size
        else:
            # 考虑[-4, -3, -2, -1] 的情况，它们应该落在一个桶中。
            # 如果直接复用 idx = nums[i] / size 的话，[-4] 和[-3, -2, -1] 会被分到不同的桶中。
            # 根本原因是我们处理整数的时候，已经分掉了数值 0。
            # 这时候我们需要先对 nums[i] 进行 + 1 操作（即将负数部分在数轴上进行整体右移），即得到(nums[i] + 1) / size。
            # 这样一来负数部分与正数部分一样，可以被正常分割了。
            # 但由于 0 号桶已经被使用了，我们还需要在此基础上进行 - 1，相当于将负数部分的桶下标（idx）往左移，即得到((nums[i] + 1) / size) - 1
            return (num+1) // size - 1


k = 1
t = 0
nums = [1, 2, 1, 1]
solution = Solution()
# print(solution.containsNearbyAlmostDuplicate1(nums, k, t))

sls = SortedList(nums)
print(sls.bisect_left(3))
