
import sys

PUNCTUATION = '.!?,-:;'

def delete_punctuation(s):

    result = ''
    for char in s:
        # Check char is not a punctuation mark
        if char not in PUNCTUATION:
            result += char          # append non-punctuation characters

    return result


def get_counts_dict(filename):

    counts = {}                             # create empty dictionary

    with open(filename, 'r') as file:       # open file for reading
        for line in file:
            words = delete_punctuation(line).split()
            for word in words:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1

    return counts


def main():

    args = sys.argv[1:]

    if len(args) == 1:
        print(get_counts_dict(args[0]))


# Python boilerplate.
if __name__ == '__main__':
    main()
