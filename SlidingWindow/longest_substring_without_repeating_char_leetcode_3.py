def longest_substring(s):
    count_map = dict()

    left = 0
    long_substring_len = 0

    for i in range(len(s)):
        if s[i] in count_map:
            if count_map[s[i]] >= left:
                left = count_map[s[i]] + 1

        count_map[s[i]] = i

        long_substring_len = max(long_substring_len, i - left + 1)

    return long_substring_len


if __name__ == '__main__':
    string = "abba"
    print(longest_substring(string))
