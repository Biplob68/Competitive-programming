from collections import deque


def calculate(s):
    number = 0
    sign = 1
    result = 0
    stack = deque()

    for i in range(len(s)):
        ch = s[i]

        if ch.isdigit():
            number = number * 10 + int(ch)

        if ch == '+' or ch == '-':
            result += number * sign
            sign = 1 if ch == '+' else -1
            number = 0

        if ch == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1

        if ch == ')':
            result += number * sign
            s_sign = stack.pop()
            result = result * s_sign
            s_result = stack.pop()
            result += s_result
            number = 0
            sign = 1

    result += number * sign
    return result


if __name__ == '__main__':
    # (1+(4+5+2)-3)+(6+8)
    ex = "1-(     -2)"
    print(calculate(ex))
