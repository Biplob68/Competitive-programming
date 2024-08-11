from collections import defaultdict


def count_repeated_dna(s):
    if len(s) < 10:
        return []
    dna_sequence_dict = defaultdict()

    ans = []
    for i in range(len(s) - 9):
        temp_string = s[i:i + 10]

        if temp_string in dna_sequence_dict:
            if temp_string not in ans:
                ans.append(temp_string)

        dna_sequence_dict[temp_string] = 1

    return ans


if __name__ == '__main__':
    dna_string = "AAAAAAAAAAA"
    # count_repeated_dna(dna_string)
    print(count_repeated_dna(dna_string))
