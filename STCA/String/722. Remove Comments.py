from typing import List


class Solution:

    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        commented = False

        newLine = []
        for line in source:
            index = 0
            # /* */ cross lines will merge to one line
            if not commented:
                newLine = []

            while index < len(line):
                if line[index:index + 2] == '//' and not commented:
                    break

                elif line[index:index + 2] == '/*' and not commented:
                    commented = True
                    index += 2

                elif line[index:index + 2] == '*/' and commented:
                    commented = False
                    index += 2

                elif not commented and index < len(line):
                    newLine.append(line[index])
                    index += 1

                else:
                    index += 1

            if newLine and not commented:
                res.append(''.join(newLine))

        return res


source = ["a/*comment", "line", "more_comment*/b"]

slt = Solution()
print(slt.removeComments(source))