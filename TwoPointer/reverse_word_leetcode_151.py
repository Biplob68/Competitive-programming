def reverse_word(str):
    index = len(str) - 1
    final_string = ""
    temp = ""

    while index >= 0:

        while index >= 0 and str[index] == ' ':
            index -= 1
        while index >= 0 and str[index] != ' ':
            temp += str[index]
            index -= 1

        final_string += temp[::-1]
        if index >= 0: final_string += " "
        temp = ""
        index -= 1

    return final_string


if __name__ == '__main__':
    str = "a good   example"
    print(reverse_word(str))
