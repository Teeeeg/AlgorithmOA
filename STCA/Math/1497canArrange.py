from typing import List


class Solution:
    # 统计余数

    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        dct = {}
        for i in range(n):
            arr[i] = arr[i] % k

        for num in arr:
            dct[num] = dct.get(num, 0) + 1

        for key in dct.keys():
            # 余数为0的可以不考虑
            if key != 0:
                # 若对立余数不存在
                if k - key not in dct:
                    return False
                # 对立余数的数量不同
                if dct[key] != dct[k - key]:
                    return False
                # 若对立余数和现在是是一样的
                # 那肯定统计是相同的
                if key == k - key:
                    # 因此，应该这个次数为偶数才行
                    if dct[key] % 2:
                        return False

        return True


arr = [5, 5, 1, 2, 3, 4]
k = 10
slt = Solution()
print(slt.canArrange(arr, k))
