# Approach:1 -> Run time Exception
"""""
def max_sliding_window(nums, k):
    if k == 1:
        return nums

    ans = []

    temp = nums[0:k]
    max_val = find_max(temp, k)
    ans.append(max_val)

    for i in range(k, len(nums)):
        temp.pop(0)
        temp.append(nums[i])
        ans.append(find_max(temp, k))

    return ans
    
def find_max(array, k):
    max_num = array[0]
    for i in range(1, k):
        if array[i] > max_num:
            max_num = array[i]
    return max_num

"""""

from collections import deque


# Approach 2: With Queue
def max_sliding_window(nums, k):
    queue = deque()

    result = []

    for i in range(len(nums)):
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()

        if queue and queue[0] <= i - k:
            queue.popleft()

        queue.append(nums[i])

        if i >= k - 1:
            result.append(queue[0])
    return result


if __name__ == '__main__':
    input_nums = [1, -1]
    k = 2
    max_window = max_sliding_window(input_nums, k)
    print(max_window)
