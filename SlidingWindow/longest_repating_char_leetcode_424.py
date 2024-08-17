from collections import defaultdict


def longest_repeating_char_replacement(s, k):
    start = 0
    long_replace = 0
    cnt_map = defaultdict(int)

    max_freq = 0

    for i in range(len(s)):
        # if s[i] not in cnt_map:
        #     cnt_map[s[i]] = 1
        # else:
        cnt_map[s[i]] += 1

        max_freq = max(max_freq, cnt_map[s[i]])

        if i - start + 1 - max_freq > k:
            cnt_map[s[start]] -= 1
            start += 1

        long_replace = max(long_replace, i - start + 1)

    return long_replace


if __name__ == '__main__':
    array = "ABAB"
    k = 1
    print(longest_repeating_char_replacement(array, k))
