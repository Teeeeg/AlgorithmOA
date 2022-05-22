def flip_and_invert_image(matrix):
    lenCol = len(matrix[0])

    for row in matrix:
        row.reverse()
        for i in range(lenCol):
            row[i] = row[i] ^ 1

    return matrix


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
