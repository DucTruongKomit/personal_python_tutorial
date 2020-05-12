# Cannot import text wrap anymore, textwrap3 is a downport of textwrap
from textwrap3 import fill, wrap


# a_string = 'This is a very very very very long sentence.'
# print(wrap(a_string, 4))
#
# print(fill(a_string, 8))


def wrap_text(string, max_width):
    return '\n'.join(wrap(string, max_width))


if __name__ == '__main__':
    string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    max_width = 4
    result = wrap_text(string, max_width)
    print(result)
