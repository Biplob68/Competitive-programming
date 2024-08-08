def isValidAbbreviation(word, abbr):
    abbr_index = 0
    word_index = 0

    while abbr_index < len(abbr):
        if abbr[abbr_index].isnumeric():
            if abbr[abbr_index] == '0':
                return False

            num = 0
            while abbr_index < len(abbr) and abbr[abbr_index].isnumeric():
                num = 10 * num + int(abbr[abbr_index])
                abbr_index += 1

            word_index += num

        else:
            if word_index >= len(word) or word[word_index] != abbr[abbr_index]:
                return False

            word_index += 1
            abbr_index += 1

    return word_index == len(word) and abbr_index == len(abbr)


if __name__ == '__main__':
    word = "internationalization"
    abbr = "13iz4n"

    print(isValidAbbreviation(word, abbr))
