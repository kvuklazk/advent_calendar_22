input_file = [i for i in open("input.txt", "r").readline()]


def char_repeats(rep_char):
    if any([i in rep_char[:rep_char.index(i)] + rep_char[rep_char.index(i)+1:] for i in rep_char]):
        return True

    return False


processed_chars = 0
print(input_file[processed_chars:processed_chars+4])
while char_repeats(input_file[processed_chars:processed_chars+4]):
    processed_chars += 1

processed_chars += 4
print(processed_chars)
