def getFactors(num):
    if num == 1:
        return []

    factors = []
    factor = 1

    while factor * factor <= num:
        if num % factor == 0:
            factors.append(factor)

            if not factor * factor == num:
                factors.append(num // factor)

        factor += 1

    return factors


print(getFactors(12))
