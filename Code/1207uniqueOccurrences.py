from typing import List


class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1

        st = set()
        for count in counter.values():
            if count in st:
                return False
            st.add(count)

        return True