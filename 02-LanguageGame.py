def lang_game():
    inp_lang = input("Pleace input language: ")
    inp_word = input("Pleace input a word: ")

    lang = inp_lang.split('^n')
    lang.pop()

    # for index, char in enumerate(inp_lang):
    #     if char == 'n':
    #         lang.append(char[index-2])

    last_char = ''
    prev_chars = ''
    num_chars = []
    index_num = -1

    for char in inp_word:
        if char != last_char:
            prev_chars += last_char
            num_chars.append(0)
            index_num += 1

        if char in prev_chars:
            return 'No'

        num_chars[index_num] += 1
        last_char = char

    prev_chars += last_char

    for i, num in enumerate(num_chars):
        if i == 0:
            continue
        if len(lang) != len(prev_chars):
            return 'No'
        elif num_chars[i] != num_chars[i - 1]:
            return 'No'
        else:
            return 'Yes'


def main():
    print(lang_game())


if __name__ == '__main__':
    main()
