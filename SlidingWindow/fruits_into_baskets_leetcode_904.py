from collections import defaultdict


def max_pick(fruits):
    cnt_map = defaultdict()
    start = 0
    max_fruit = 0

    for i in range(len(fruits)):
        if fruits[i] not in cnt_map:
            cnt_map[fruits[i]] = 1
        else:
            cnt_map[fruits[i]] += 1

        while len(cnt_map) > 2:
            temp = fruits[start]
            cnt_map[temp] -= 1
            if cnt_map[temp] == 0:
                cnt_map.pop(temp)
            start += 1

        max_fruit = max(max_fruit, i - start + 1)

    return max_fruit


if __name__ == '__main__':
    # nums = [3, 3, 3, 1, 2, 1, 0, 2, 3, 3, 4]
    # nums = [1, 2, 3, 2, 2]
    # nums = [0, 1, 2, 2]
    nums = [1, 0, 1, 4, 1, 4, 1, 2, 3]
    print(max_pick(nums))
