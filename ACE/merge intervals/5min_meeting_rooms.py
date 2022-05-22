from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # 重写比较器
    def __lt__(self, other):
        return self.end <= other.end


# 用miniHeap保存正在开会的会议室
# 意味着
# 当前的会议时间与miniHeap中end最小的比较
# 如果大于等于最小的，说明可以复用
# 否则需要创建新的会议室

def min_meeting_rooms(meetings: Meeting):
    res = 0
    miniHeap = []
    meetings.sort(key=lambda x: x.start)

    for meeting in meetings:
        # 如果未重叠，则接在最先结束的会议后面
        while miniHeap and meeting.start >= miniHeap[0].end:
            heappop(miniHeap)
        # 有重叠，则添加新的会议室
        heappush(miniHeap, meeting)
        res = max(len(miniHeap), res)

    return res

# Time O(nlogn)
# Space O(n)


def main():
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()
