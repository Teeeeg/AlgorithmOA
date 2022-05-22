def find_substring(str1, pattern):
    n = len(str1)
    n1 = len(pattern)
    win_start = 0
    patternCounter = {}
    match = 0
    res = 'x'*(n+1)

    for s in pattern:
        if s not in patternCounter:
            patternCounter[s] = 0
        patternCounter[s] += 1

    for win_end in range(n):
        right_chr = str1[win_end]
        if right_chr in patternCounter:
            patternCounter[right_chr] -= 1
            if patternCounter[right_chr] >= 0:
                match += 1

        while match == n1:
            res = str1[win_start: win_end +
                       1] if len(res) > (win_end-win_start+1) else res
            left_chr = str1[win_start]
            if left_chr in patternCounter:
                if patternCounter[left_chr] == 0:
                    match -= 1
                patternCounter[left_chr] += 1
            win_start += 1

    return "" if len(res) > n else res


String = "aadec"
Pattern = "abc"
print(find_substring(String, Pattern))
