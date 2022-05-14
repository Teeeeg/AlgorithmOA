class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        strs = date.split('-')
        year = int(strs[0])
        month = int(strs[1])
        day = int(strs[2])

        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month > 2:
            return sum(months[: month-1]) + day + 1
        else:
            return sum(months[: month-1]) + int(day)


date = "2000-01-31"
solution = Solution()
print(solution.dayOfYear(date))
