from collections import deque


def valid_parentheses(s):
    stack = deque()

    for i in range(len(s)):
        if stack and (s[i] == ')' and stack[-1][0] == '('):
            stack.pop()
        elif s[i] in "()":
            stack.append([s[i], i])
    ans = ""

    for i in range(len(s)):
        if stack and s[i] == stack[0][0] and i == stack[0][1]:
            stack.popleft()
        else:
            ans += s[i]

    return ans


if __name__ == '__main__':
    input_str = "))(("
    print(valid_parentheses(input_str))
