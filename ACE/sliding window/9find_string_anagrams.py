def find_string_anagrams(str1, pattern):
    n = len(str1)
    n1 = len(pattern)
    win_start = 0
    counter = {}
    patternCounter = {}
    res = []

    for s in pattern:
        if s not in patternCounter:
            patternCounter[s] = 0
        patternCounter[s] += 1

    for win_end in range(n):
        right_chr = str1[win_end]
        if right_chr not in counter:
            counter[right_chr] = 0
        counter[right_chr] += 1

        if win_end - win_start + 1 >= n1:
            left_chr = str1[win_start]
            if patternCounter == counter:
                res.append(win_start)
            counter[left_chr] -= 1
            if counter[left_chr] == 0:
                del counter[left_chr]
            win_start += 1

    return res


String = "abbcabc"
Pattern = "abc"
print(find_string_anagrams(String, Pattern))
