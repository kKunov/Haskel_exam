def get_known_m_f():
    known_m_f = [0, 0]

    known_m_f[0] = input("Males names: ")
    known_m_f[1] = input("females names: ")

    known_m_f[0] = int(known_m_f[0])  # Tuk gi preobrazuvam za da moga
    known_m_f[1] = int(known_m_f[1])  # sled tova da gi polzvam bez da go pravq

    return known_m_f


def helper_get_names():
    name = input("Input Name or 'no' for no more names: ")
    is_ends_with_correct = (
        name == 'no' or
        name.endswith('ss') or
        name.endswith('tta')
    )
    while is_ends_with_correct is False:
        name = input("Its not valid name, try again:")
        is_ends_with_correct = (
            name == 'no' or
            name.endswith('ss') or
            name.endswith('tta')
        )
    return name


def get_names():
    names = []
    names.append(helper_get_names())

    while names[len(names) - 1] != 'no':
        names.append(helper_get_names())

    names.pop()  # tuk pop-vam posledniq element za da e po-chist
    # masiva zashtoto realno posledniq element e "no"
    return names


def name_maching(known_m_f, names):
    num_males = 0
    num_females = 0

    for name in names:

        if name.endswith('ss'):
            num_males += 1

        elif name.endswith('tta'):
            num_females += 1

    unknown_males = num_males - known_m_f[0]
    unknown_females = num_females - known_m_f[1]

    male_percentage = 1 / unknown_males
    female_percentage = 1 / unknown_females

    print("%s   %s" % (male_percentage, female_percentage,))

    percentage = 1 * male_percentage * female_percentage
    percentage *= 100
    print("%s percent" % (percentage,))


def main():
    known_m_f = get_known_m_f()

    names = get_names()

    name_maching(known_m_f, names)


if __name__ == '__main__':
    main()
