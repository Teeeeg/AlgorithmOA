from heapq import *
from typing import List


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    # 比较器，堆顶保持最先完成的任务
    def __lt__(self, other):
        self.end <= other.end


def find_max_cpu_load(jobs: List):
    miniHeap = []
    cur = 0
    res = 0
    jobs.sort(key=lambda x: x.start)

    for job in jobs:
        # 不重叠，则替换最先结束的任务
        while miniHeap and job.start >= miniHeap[0].end:
            # 减去替换掉的任务
            cur -= miniHeap[0].cpu_load
            heappop(miniHeap)
        # 加上新增的任务
        cur += job.cpu_load
        heappush(miniHeap, job)

        res = max(cur, res)

    return res


# Time O(nlogn)
# Space O(n)

def main():
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
