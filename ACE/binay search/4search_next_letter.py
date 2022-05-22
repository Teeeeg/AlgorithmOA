def search_next_letter(letters, key):
    n = len(letters)
    ord_key = ord(key)

    l, r = 0, n-1
    while l <= r:
        mid = (l+r) // 2
        if ord(letters[mid]) > ord_key:
            r = mid-1
        # 寻找key大的，则忽略==的情况
        else:
            l = mid+1

    # 循环链表
    return letters[l % n]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
