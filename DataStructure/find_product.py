def find_product(lst):
    n = len(lst)
    res = []
    leftProd = 1

    for i in range(n):
        righrProd = 1
        for j in range(i+1, n):
            righrProd *= lst[j]
        res.append(leftProd * righrProd)
        leftProd *= lst[i]

    return res


arr = [1, 2, 3, 4]
print(find_product(arr))
