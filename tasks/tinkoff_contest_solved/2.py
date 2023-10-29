def read_input():
    s = input()
    return s


def find_the_maximum_number_of_words(s):
    letter_dict = {
        's': 0,
        'h': 0,
        'e': 0,
        'r': 0,
        'i': 0,
        'f': 0,
    }
    for letter in s:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1

    letter_dict['f'] //= 2

    return min(letter_dict.values())


def main():
    print(find_the_maximum_number_of_words(read_input()))


if __name__ == '__main__':
    main()
