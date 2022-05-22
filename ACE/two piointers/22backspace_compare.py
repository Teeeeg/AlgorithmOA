# 利用栈
def backspace_compare(str1, str2):
    def applyBackspace(original: str):
        n = len(original)
        res = []
        for i in range(n):
            if original[i] == '#':
                res.pop()
            else:
                res.append(original[i])
        return ''.join(res)

    str1 = applyBackspace(str1)
    str2 = applyBackspace(str2)

    return str1 == str2

# Time O(n)
# Time O(n)


# 分别两个指针
def backspace_compare1(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    p1 = n1-1
    p2 = n2-1

    def getNext(original: str, p: int):
        count = 0
        while original[p] == '#':
            count += 1
            p -= 1
        for _ in range(count):
            p -= 1
        return p

    while p1 >= 0 or p2 >= 0:
        p1 = getNext(str1, p1)
        p2 = getNext(str2, p2)

        if str1[p1] != str2[p2]:
            return False

        p1 -= 1
        p2 -= 1

    return True


str1 = "xy#"
str2 = "xz##"
print(backspace_compare1(str1, str2))
