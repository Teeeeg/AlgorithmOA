def longest_substring_with_k_distinct(str1, k):
    n = len(str1)
    dic = {}
    res = 0
    win_start = 0

    for win_end in range(n):
        right_chr = str1[win_end]
        if right_chr not in dic:
            dic[right_chr] = 0
        dic[right_chr] += 1

        while len(dic) > k:
            left_chr = str1[win_start]
            dic[left_chr] -= 1
            if dic[left_chr] == 0:
                del dic[left_chr]
            win_start += 1

        res = max(res, win_end-win_start+1)

    return res


str1 = "araaci"
K = 2
print(longest_substring_with_k_distinct(str1, K))
