def maximum_points(cardPoints, k):
    size = len(cardPoints) - 1

    max_sum = 0
    for i in range(0, k):
        max_sum += cardPoints[i]

    window_sum = max_sum

    for i in range(k):
        window_sum -= cardPoints[k - 1 - i]
        window_sum += cardPoints[size - i]

        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    max_sum = maximum_points(array, k)
    print(max_sum)
