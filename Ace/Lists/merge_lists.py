def merge_lists(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    res = []

    i, j = 0, 0
    while i < n1 and j < n2:
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1

    if i < n1:
        res += lst1[i:]
    if j < n2:
        res += lst2[j:]

    return res


def merge_lists1(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    i, j = 0, 0
    while i < n1 and j < n2:
        if lst1[i] > lst2[j]:
            lst1.insert(i, lst2[j])
            i += 1
            j += 1
        else:
            i += 1

    if j < n2:
        lst1 += lst2[j:]

    return lst1


list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]
print(merge_lists1(list1, list2))
