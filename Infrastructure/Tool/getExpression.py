from termios import VLNEXT


def getExpression(s):
    expression = []
    # use None, because if ( shows, it may not have number in front of it
    val = None

    for char in s:
        if char == ' ':
            continue

        if char in ['+', '-', '*', '/', '(', ')']:
            # prevous has a number
            if val is not None:
                expression.append(val)
            val = None
            expression.append(char)

        else:
            # initial a number
            if val is None:
                val = 0
            val = val * 10 + ord(char) - ord('0')

    # last number
    if val is not None:
        expression.append(val)

    return expression


def getExpression1(s):
    expression = []
    # use None, because if ( shows, it may not have number in front of it
    n = len(s)
    i = 0

    while i < n:
        char = s[i]

        if char == ' ':
            i += 1
        elif char in ['+', '-', '*', '/', '(', ')']:
            expression.append(char)
            i += 1
        else:
            val = 0
            while i < n and s[i].isnumeric():
                val = val * 10 + int(s[i])
                i += 1

            expression.append(str(val))

    return expression


s = "1*2-3/4+5*6-7*8+9/10"
print(getExpression1(s))
