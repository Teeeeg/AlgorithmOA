def find_letter_case_string_permutations(str):
    permutations = [str]
    n = len(str)

    # 处理的字符index
    for i in range(n):
        # 只处理字母
        if str[i].isalpha():
            n1 = len(permutations)
            # 遍历所有permutation
            for _ in range(n1):
                # 两种变化
                # 1. 不变
                pre = permutations.pop(0)
                permutations.append(pre)
                # 2. 变case
                pre = list(pre)
                pre[i] = pre[i].swapcase()
                permutations.append(''.join(pre))

    return permutations


# Time O(n*2^n)
# Space O(n*2^n)

def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
