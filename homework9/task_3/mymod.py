from os import path


def count_lines(file_name):
    if path.isfile(file_name):
        with open(file_name) as file:
            return len(file.readlines())
    else:
        print(f'File {file_name} does not exist')


def count_chars(file_name):
    if path.isfile(file_name):
        with open(file_name) as file:
            return len(file.read())
    else:
        print(f'File {file_name} does not exist')


def test(file_name):
    lines = count_lines(file_name)
    chars = count_chars(file_name)
    return lines, chars
