def non_repeat_substring(str):
    n = len(str)
    lookup = set()
    win_start = 0
    res = 0

    for win_end in range(n):
        right_chr = str[win_end]
        if right_chr not in lookup:
            lookup.add(right_chr)
        else:
            while right_chr in lookup:
                left_chr = str[win_start]
                lookup.remove(left_chr)
                win_start += 1
            lookup.add(right_chr)

        res = max(res, len(lookup))

    return res

    # n = len(str)
    # dic = {}
    # res = 0
    # win_start = 0

    # for win_end in range(n):
    #     right_chr = str[win_end]
    #     if right_chr not in dic:
    #         dic[right_chr] = win_end
    #     else:
    #         win_start = dic[right_chr]+1
    #     dic[right_chr] = win_end
    #     res = max(res, win_end-win_start+1)
    # return res


String = "abccde"
print(non_repeat_substring(String))
