from heapq import heappop, heappush


def schedule_tasks(tasks, k):
    dct = {}
    maxHeap = []
    res = 0

    for task in tasks:
        dct[task] = dct.get(task, 0) + 1

    for task, freq in dct.items():
        heappush(maxHeap, (-freq, task))

    while maxHeap:
        # queue表示等待队列
        waitList = []
        # 中间k个task，则到运行k+1个之后才可以运行
        n = k+1

        while n > 0 and maxHeap:
            res += 1
            freq, task = heappop(maxHeap)
            if -freq > 1:
                waitList.append((freq+1, task))
            n -= 1

        # 若还有任务则需要等待
        if waitList:
            res += n

        for freq, task in waitList:
            heappush(maxHeap, (freq, task))

    return res


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
