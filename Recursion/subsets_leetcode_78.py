def subsets(input_array, index, subarray):
    if index == len(input_array):
        print(subarray)

    else:
        subsets(input_array, index + 1, subarray)
        subsets(input_array, index + 1, subarray + [input_array[index]])


if __name__ == '__main__':
    numbers = [1, 2, 3]

    subsets(numbers, 0, [])
