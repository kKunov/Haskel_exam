#  Nqma Space-ove mejdu bukvite zashtoto reshih che po-lesno se testva bez tqh


def inp():
    paths = []
    i = 0

    paths.append(input("pleace insert 2 station: "))

    while paths[i] != '':
        paths.append(input("pleace insert 2 station: "))
        i += 1

    paths.pop()
    return paths


def helper(paths):
    first_path = ''
    last_path = ''
    finale_path = ''
    i = 0

    while first_path == '' and i < len(paths):
        if paths[i].startswith('H'):
            first_path = paths[i]
        i += 1

    if first_path == '':
        print("ERROR: Bad input: No 'H' station!")
        return

    i = 0

    while last_path == '' and i < len(paths):
        if paths[i].endswith('L'):
            last_path = paths[i]
        i += 1

    if last_path == '':
        print("ERROR: Bad input: No 'L' station!")
        return

    i = 0

    while finale_path.endswith('L') is False:
        if finale_path == '':
            finale_path = first_path

        for path in paths:
            if finale_path.endswith(path[0]):
                finale_path += path[1]
            if path == 'HL':
                finale_path = path

    print(finale_path)


def main():
    paths = inp()
    helper(paths)


if __name__ == '__main__':
    main()
