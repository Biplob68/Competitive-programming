from collections import defaultdict


def arrayRankTransform(arr):
    temp = arr.copy()
    arr.sort()

    cnt = 1
    result = []

    rank = defaultdict()
    rank[arr[0]] = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            cnt += 1
        rank[arr[i]] = cnt

    for i in range(len(temp)):
        result.append(rank[temp[i]])

    return result


if __name__ == '__main__':
    array = [40, 10, 20, 30]
    print(arrayRankTransform(array))
