from typing import List


class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        file2Count = {}
        res = []

        for name in names:
            if name not in file2Count:
                res.append(name)
                file2Count[name] = 1
            else:
                curName = name + '(' + str(file2Count[name]) + ')'
                file2Count[name] = file2Count[name] + 1

                while curName in file2Count:
                    curName = name + '(' + str(file2Count[name]) + ')'
                    file2Count[name] = file2Count[name] + 1

                file2Count[curName] = 1
                res.append(curName)

        return res


names = ["wano", "wano", "wano", "wano"]
slt = Solution()
print(slt.getFolderNames(names))
