def merge_sorted_array(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = len(nums1) - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    return nums1


if __name__ == '__main__':
    nums1 = [2, 3, 0, 0]
    m = 2
    nums2 = [1, 4]
    n = 2

    nums1 = merge_sorted_array(nums1, m, nums2, n)
    print(nums1)
