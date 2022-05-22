def pair_with_targetsum(arr, target_sum):
    n = len(arr)
    l, r = 0, n-1

    while l <= r:
        pair_sum = arr[l] + arr[r]
        if pair_sum == target_sum:
            return [l, r]
        if pair_sum < target_sum:
            l += 1
        else:
            r -= 1

    return []
