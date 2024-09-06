# Approach 1: Using sort function

"""
def kth_smallest_element(matrix, k):
    sorted_array = []

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            sorted_array.append(matrix[i][j])

    sorted_array.sort()
    return sorted_array[k - 1]
"""

# Approach 2: Using heap
# Time Complexity : O( m+k log(m) )
from heapq import heappush, heappop


def kth_smallest_element(matrix, k):
    n = len(matrix[0])

    sorted_list = []

    for i in range(len(matrix)):
        heappush(sorted_list, (matrix[i][0], i, 0))

    top_element = sorted_list[0]
    while k > 0:
        top_element, row, col = heappop(sorted_list)
        if col < n - 1:
            heappush(sorted_list, (matrix[row][col + 1], row, col + 1))
        k -= 1

    return top_element


if __name__ == '__main__':
    matrix = [[1, 2], [1, 3]]
    k = 2
    print(kth_smallest_element(matrix, k))
