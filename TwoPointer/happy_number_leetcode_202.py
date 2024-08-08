def isHappyNumber(num):
    slow = find_square_sum(num)
    fast = find_square_sum(find_square_sum(num))

    while fast != 1 and slow != fast:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
    if fast == 1:
        return True
    return False


def find_square_sum(n):
    s = 0
    if n % 10 == n:
        return n * n
    while n > 0:
        s += (n % 10) * (n % 10)
        n = n // 10
    return s


if __name__ == '__main__':
    print(isHappyNumber(4))
