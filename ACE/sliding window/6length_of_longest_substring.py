def length_of_longest_substring(str1, k):
    n = len(str1)
    dic = {}
    win_start = 0
    count = 0
    res = 0

    # 窗口总大小-重复的元素大小
    # 满足题意则记录
    # 不满足则从左边开始缩小

    for win_end in range(n):
        right_chr = str1[win_end]
        if right_chr not in dic:
            dic[right_chr] = 0
        dic[right_chr] += 1
        count = max(count, dic[right_chr])
        win_len = win_end - win_start + 1

        # 每次缩小完必须回去更新count
        # 同步滑动，因为无需考虑窗口大小比上一次不满足条件的情况
        # 题目只要最大值
        if win_len - count > k:
            left_chr = str1[win_start]
            dic[left_chr] -= 1
            win_start += 1

        res = max(res, win_end-win_start+1)
    return res


String = "aabccbb"
k = 2
print(length_of_longest_substring(String, k))
