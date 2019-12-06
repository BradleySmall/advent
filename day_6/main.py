"""Day 6: Universal Orbit Map."""


def get_maps():
    """Read in the list of maps."""
    with open("input.txt") as f:
        return [line.rstrip("\n").split(")") for line in f.readlines()]


def main():
    """Drive the main program."""
    maps = get_maps()
    # print(maps[:5])
    my_dict = {}
    for v, k in maps:
        my_dict[k] = v

    dict_cnt = {}
    for m in my_dict:
        i = 0
        v = my_dict[m]
        while v:
            i += 1
            v = my_dict.get(v, 0)
        dict_cnt[m] = i
        # print(f'{m}->{i}')

    dict_us = {}
    for m in "SAN", "YOU":
        path = []
        v = my_dict[m]
        while v:
            path.append(v)
            v = my_dict.get(v, 0)
        dict_us[m] = path

    # print(sum(dict_cnt.values()))
    # print(my_dict['YOU'], my_dict['SAN'])
    # print(dict_us)
    r = [
        a for a, b in zip(reversed(dict_us["YOU"]),
                          reversed(dict_us["SAN"])) if a == b
    ]
    # print (r)
    for k in dict_us:
        dict_us[k] = [a for a in dict_us[k] if a not in r]

    print(my_dict["YOU"], my_dict["SAN"])
    print(len(dict_us["YOU"]) + len(dict_us["SAN"]))


if __name__ == "__main__":
    main()
