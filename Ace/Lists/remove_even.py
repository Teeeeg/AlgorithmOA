def remove_even(lst):
    n = len(lst)
    res = []
    for i in range(n):
        if lst[i] % 2:
            res.append(lst[i])

    return res


my_list = [1, 2, 4, 5, 10, 6, 3]
print(remove_even(my_list))
