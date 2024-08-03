def sort_color(nums):
    left = 0
    right = len(nums) - 1
    index = 0

    while index < right:
        if nums[index] == 0:
            swap(nums, left, index)
            left += 1
            index += 1

        elif nums[index] == 2:
            swap(nums, index, right)
            right -= 1

        else:
            index += 1

    return nums


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == '__main__':
    input_array = [1, 1, 2, 0, 0, 1, 2, 1, 1, 0]

    print(sort_color(input_array))
