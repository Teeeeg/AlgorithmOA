def calculate_bitwise_complement(n):
    bitCount = 0
    while n:
        bitCount += 1
        n = n >> 1

    # 所有位数置1
    # 2^4-1有4个1 (16-1)
    allBitsSet = pow(2, bitCount)-1

    return n ^ allBitsSet


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()
