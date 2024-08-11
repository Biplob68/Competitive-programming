def max_consecutive_one(nums, k):
    left = 0
    max_one = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            k -= 1

        while k < 0:
            if nums[left] == 0:
                k += 1
            left += 1

        max_one = max(max_one, i - left + 1)

    return max_one


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(max_consecutive_one(nums, k))
