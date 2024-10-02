def combination_sum(index, candidates, curr, target, total, result):
    if total == target:
        result.append(curr.copy())
        return
    if index >= len(candidates) or total > target:
        return

    curr.append(candidates[index])
    combination_sum(index, candidates, curr, target, total + candidates[index], result)
    curr.pop()
    combination_sum(index + 1, candidates, curr, target, total, result)


if __name__ == '__main__':
    array = [2, 3, 6, 7]
    target = 7
    result = []
    combination_sum(0, array, [], target, 0, result)
    print(result)
