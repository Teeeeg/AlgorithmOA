class ParenthesesString:
    def __init__(self, string: str, openCount: int, closeCount: int) -> None:
        self.string = string
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):
    res = []
    queue = []
    queue.append(ParenthesesString('', 0, 0))

    # num >= open >= close

    # 广度优先
    while queue:
        ps = queue.pop(0)
        # 当左右括号都等于num时候则记录答案
        if ps.openCount == num and ps.closeCount == num:
            res.append(ps.string)
        else:
            if ps.openCount < num:
                queue.append(ParenthesesString(
                    ps.string + '(', ps.openCount+1, ps.closeCount))  # O(n)连接字符串
            # 右括号不可以大于左括号
            if ps.openCount > ps.closeCount:
                queue.append(ParenthesesString(ps.string+')',
                             ps.openCount, ps.closeCount+1))
    return res


# Time O(n*2^n)
# Space O(n*2^n)


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
