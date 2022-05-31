from typing import List


class Solution:
    # 同余定理
    # (sum[i] - sum[j]) % k == 0 等价于 sum[i] % k == sm[j] % k

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dct = {0: 1}
        total = 0
        res = 0

        for num in nums:
            total += num
            # 记录余数
            mod = total % k
            res += dct.get(mod, 0)
            dct[mod] = dct.get(mod, 0) + 1

        return res


nums = [4, 5, 0, -2, -3, 1]
k = 5
slt = Solution()
print(slt.subarraysDivByK(nums, k))
