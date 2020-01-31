"""
Example file for building a python list from a wordlist in format of name per line.
"""

TARGET_PY_FILE = 'word_lists.py'
WORD_FILE = 'shields.txt'


def build_list_from_word_list(py_file, word_file, list_name):
    with open(word_file) as f:
        items = f.readlines()

    with open(py_file, 'a+') as f:
        f.write("%s = [\n    " % list_name)
        count = 0
        first = True
        for item in sorted(items):
            if not first:
                f.write(", ")
            first = False
            if count > 5:
                f.write('\n    ')
                count = 0
            f.write("\"%s\"" % item.replace('\n', ''))
            count += 1
        f.write(']\n\n')


if __name__ == "__main__":
    _py_file = input("Enter target py file for output: ") or TARGET_PY_FILE
    _word_file = input("Enter output file:") or WORD_FILE
    _list_name = input("Enter list name for target py: ")
    build_list_from_word_list(_py_file, _word_file, _list_name)

