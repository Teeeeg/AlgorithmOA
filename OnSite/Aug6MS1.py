# You are given a task to fix potholes in a road. The road is
# described by a string S consisting of N characters. Each character
# represents a single fragment of the road. Character " denotes a
# smooth surface and 'x' denotes a pothole. For example, S=
# ..xxx..x means that the road starts with three smooth fragments,
# followed by three potholes, followed by two smooth fragments
# and ending with one pothole.
# You can choose an number of consecutive potholes and fix all of
# them. Fixing a segment consisting of K consecutive potholes
# costs K + 1. In the example above, fixing the first two consecutive
# potholes costs 2 + 1 = 3 and fixing the last pothole costs 1 + 1 = 2.
# After these fixes the road would look like this:"
# '.....X..
# You are given a budaet B. You can fix multiple segments
# containing potholes as long as you fit in the budget. What is the
# maximum number of potholes vou can fix?
# Write a function:
# def solutions, B)
# that, given the string S of length N and the integer B, returns the
# maximum number of potholes that can be fixed.


def solution(S, B):
    if not S or not B:
        return 0

    n = len(S)
    counts = []
    left = 0
    while left < n:
        if S[left] == 'x':
            right = left
            while right < n and S[right] != '.':
                right += 1
            counts.append(right - left)
            left = right
        left += 1

    counts.sort(reverse=True)
    res = 0

    for count in counts:
        if count + 1 <= B:
            B -= count + 1
            res += count
        else:
            res += B - 1
            break

    return res


S = 'xxx..x..xxx'
B = 7
print(solution(S, B))