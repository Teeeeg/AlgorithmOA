# 两个错误条件
# 1. 方向相反
# 2. 环内只有一个自己

def circular_array_loop_exists(arr):
    n = len(arr)
    visited = set()

    def getNext(isForward: bool, curIndex):
        dir = arr[curIndex] >= 0
        # 如果方向相反，则跳过
        if isForward != dir:
            return -1
        # 下一个目标
        nextIndex = (curIndex + arr[curIndex]) % n
        if nextIndex == curIndex:
            return -1
        return nextIndex

    # 从每一个点出发，尝试
    for i in range(n):
        isForward = arr[i] >= 0
        slow = fast = i

        # 快慢指针判断是否有环
        while True:
            slow = getNext(isForward, slow)
            fast = getNext(isForward, fast)

            if fast != -1:
                fast = getNext(isForward, fast)

            if fast in visited:
                break
            visited.add(fast)

            # 弹出死循环
            if fast == -1 or slow == -1 or slow == fast:
                break

        if fast == slow and slow != -1:
            return True

    return False

# Time O(n2)


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
