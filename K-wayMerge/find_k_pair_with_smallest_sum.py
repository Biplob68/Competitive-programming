from heapq import heappush, heappop


def find_k_pair_smallest_sum(nums1, nums2, k):
    min_heap = []
    smallest_k_pair = []

    for i in range(len(nums1)):
        heappush(min_heap, (nums1[i] + nums2[0], i, 0))

    while min_heap and k > 0:
        sum_val, i, j = heappop(min_heap)
        smallest_k_pair.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):
            heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        k -= 1

    return smallest_k_pair


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    print(find_k_pair_smallest_sum(nums1, nums2, k))
