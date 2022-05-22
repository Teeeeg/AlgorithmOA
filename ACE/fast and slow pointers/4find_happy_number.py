def find_happy_number(num: int):
    def getNext(num: int):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total

    slow = fast = num
    while slow != 1:
        slow = getNext(slow)
        fast = getNext(getNext(fast))
        if slow == fast and slow != 1:
            return False

    return True

# Time O(logn)


num = 23
print(find_happy_number(num))
