
if __name__ == '__main__':
    # s = input()
    s = 'qA2'
    if any(x.isalnum() for x in s):
        print(True)
    else:
        print(False)

    if any(x.isalpha() for x in s):
        print(True)
    else:
        print(False)

    if any(x.isdigit() for x in s):
        print(True)
    else:
        print(False)

    if any(x.islower() for x in s):
        print(True)
    else:
        print(False)

    if any(x.isupper() for x in s):
        print(True)
    else:
        print(False)
