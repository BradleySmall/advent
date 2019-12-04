""" Document Comment """
def meets_criteria(num):
    list_num = list(str(num))
    if not (list_num[0] <= \
        list_num[1] <= \
        list_num[2] <= \
        list_num[3] <= \
        list_num[4] <= \
        list_num[5]):
            return False

    if  not (list_num[0] == list_num[1]\
        or\
        list_num[1] == list_num[2]\
        or\
        list_num[2] == list_num[3]\
        or\
        list_num[3] == list_num[4]\
        or\
        list_num[4] == list_num[5]):
            return False

    count = {}
    for i in list_num:
        count[str(i)] = count.get(str(i), 0) + 1

    if any(v == 2 for v in count.values()):
        return True
    return False


def main():
    """ Function Comment """
    bf_tries = []
    for x in range(353096, 843212+1):
        if meets_criteria(x):
            bf_tries.append(x)

    print(bf_tries)
    print(len(bf_tries))


if __name__ == "__main__":
    main()

