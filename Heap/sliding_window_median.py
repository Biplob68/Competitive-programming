from heapq import heappush, heappop


def sliding_window_median(nums, k):
    max_heap_small_num = []
    min_heap_larger_num = []

    result = []

    left = 0
    right = k - 1

    for i in range(len(nums)):
        if len(max_heap_small_num) == 0 or -max_heap_small_num[0] > nums[i]:
            heappush(max_heap_small_num, -nums[i])
        else:
            heappush(min_heap_larger_num, nums[i])

        if len(max_heap_small_num) > len(min_heap_larger_num) + 1:
            heappush(min_heap_larger_num, -heappop(max_heap_small_num))

        if len(min_heap_larger_num) > len(max_heap_small_num):
            heappush(max_heap_small_num, -heappop(min_heap_larger_num))

        if i >= k - 1:
            if k % 2 == 0:
                result.append((-max_heap_small_num[0] + min_heap_larger_num[0]) / 2.0)
            else:
                result.append(-max_heap_small_num[0] * 1.0)

        heappop(min_heap_larger_num(nums[left]))

    return result


if __name__ == '__main__':
    nums = [1, 4, 2, 3]
    k = 4
    print(sliding_window_median(nums, k))
