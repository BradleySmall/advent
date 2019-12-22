"""Day 10: Monitoring Station."""
import itertools
import math

def input_map():
    with open("input.txt") as f:
        lst = f.readlines()
    
    return [list(l.strip()) for l in lst]

def get_stroid_addrs(map):
    stroid_list = []
    for row, col in itertools.product(range(len(map)), range(len(map[0]))):
            if map[row][col] == '#':
                stroid_list.append((row, col))
            # print(f'row{row},col{col} {map[row][col]}')
    return stroid_list


def main():
    x = input_map()
    l = get_stroid_addrs(x)
    # print(len(l))
    ac_dict = {}
    ac_dict2 = {}

    for point in l:
        angles = set()
        for point2 in l:
            angles.add(math.atan2(point2[0] - point[0], point2[1] - point[1]))

        ac_dict[str(point)] = len(angles) 
        ac_dict2[str(point)] = angles

    print( max(ac_dict.values()))
    maxd = ''
    for d in ac_dict:
        if ac_dict[d] == 303:
            maxd = d
            break

    print(f'Max = {d}')
    point = (29, 26)

    roid_dict = {}
    for point2 in l:
       roid_dict[str(point2)] = math.atan2(point2[0] - point[0], point2[1] - point[1])
    
    print(roid_dict)

if __name__ == '__main__':
    main()
