def find_single_numbers(nums):
    # 先求所有数字的异或
    # 得到的结果是n1 ^ n2
    n1Xn2 = 0
    for num in nums:
        n1Xn2 ^= num

    # 找到n1 和 n2 不相同的一个bit
    rightBit = 1
    while not (rightBit & n1Xn2):
        rightBit = rightBit << 1
    num1 = 0
    num2 = 0

    # 用这个不同的bit来划分所有数字
    # 1. 所有数字该bit都为1
    # 2. 所有数字该bit都为0
    # 由于数字有重复项， 各个分组的异或变成落单数
    for num in nums:
        if num & rightBit != 0:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
