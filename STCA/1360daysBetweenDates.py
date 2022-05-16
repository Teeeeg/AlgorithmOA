class Solution:

    def isLeapYear(self, year):
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            return True
        return False

    def calculate(self, date):
        dateArr = [int(i) for i in date.split('-')]
        year = dateArr[0]
        month = dateArr[1]
        day = dateArr[2]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = 0

        while year > 1971 or month > 1 or day > 1:
            day -= 1
            res += 1
            if day == 0:
                month -= 1
                day = months[month - 1]
                if month == 2 and self.isLeapYear(year):
                    day += 1
            if month == 0:
                year -= 1
                month = 12

        return res

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        ts1 = self.calculate(date1)
        ts2 = self.calculate(date2)
        return abs(ts1 - ts2)


date1 = "2010-9-23"
date2 = "1971-6-29"
slt = Solution()
print(slt.daysBetweenDates(date1, date2))