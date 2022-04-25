from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        self.sortedList = SortedList(key=lambda x: x[0])

    def book(self, start: int, end: int) -> bool:
        reserve = [start, end]
        index = self.sortedList.bisect_left(reserve)

        if len(self.sortedList) == 0:
            self.sortedList.add(reserve)
            return True

        if 0 < index < len(self.sortedList):
            if self.sortedList[index-1][1] <= start and end <= self.sortedList[index][0]:
                self.sortedList.add(reserve)
                return True

        if index == 0:
            if end <= self.sortedList[index][0]:
                self.sortedList.add(reserve)
                return True

        if index == len(self.sortedList):
            if self.sortedList[index-1][1] <= start:
                self.sortedList.add(reserve)
                return True

        return False
