def four_sum(nums, target):
    result = []
    nums.sort()

    n = len(nums) - 1
    print(n)
    for i in range(0, n - 2):
        if i > 0 and nums[i] == nums[i - 1]: continue
        for j in range(i + 1, n - 1):
            if j > i + 1 and nums[j] == nums[j - 1]: continue
            left = j + 1
            right = n
            # print("i: ", i, "j: ", j, "left: ", left, "right: ", right)
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

    return result


if __name__ == '__main__':
    input_num = [2, 2, 2, 2, 2]
    target_num = 8

    ans = four_sum(input_num, target_num)
    print(ans)
