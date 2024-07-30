def threeSum(array):
    result_list = []

    length = len(array) - 1

    for i in range(0, length - 1):

        if i > 0 and array[i] == array[i - 1]:
            continue

        left = i + 1
        right = len(array) - 1

        while left < right:
            three_sum = array[i] + array[left] + array[right]
            if three_sum == 0:
                result_list.append([array[i], array[left], array[right]])

                while left < right and array[left] == array[left + 1]:
                    left += 1
                while left < right and array[right] == array[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            elif three_sum > 0:
                right -= 1

            elif three_sum < 0:
                left += 1

    return result_list


if __name__ == '__main__':
    array_list = [-1, 0, 1, 2, -1, -4]
    # result : [-1, -1, 2], [-1, 0, 1]]

    array_list.sort()
    result = threeSum(array_list)
    print(result)
