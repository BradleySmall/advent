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
        if map[row][col] == "#":
            stroid_list.append((row, col))
    return stroid_list


def main():
    x = input_map()
    l = get_stroid_addrs(x)

    ac_dict = {}
    for point in l:
        angles = set()
        for point2 in l:
            if point2 == point:
                continue
            angles.add( math.atan2(point2[0] - point[0], point2[1] - point[1]) * 180 / math.pi)

        ac_dict[point] = len(angles)

    # for k in ac_dict:
    #     print(k, ac_dict[k])
    # print(max(ac_dict.values()))

    maxd = 0
    bigd = ()
    for d in ac_dict:
        if ac_dict[d] > maxd:
            maxd = ac_dict[d]
            bigd = d

    print(f"Laser at {bigd}")
    point = bigd

    roid_dict = {}
    for point2 in l:
        if point2 == point:
            continue
        roid_angle = (math.atan2(point2[0] - point[0], point2[1] - point[1]) * 180 / math.pi)
        if roid_angle < 0:
            roid_angle += 360
        roid_dist = max(point2[0], point[0]) - min(point[0], point2[0]) + max(point2[1], point[1]) - min(point[1], point2[1])
        roid_dict.setdefault(roid_angle, []).append((roid_dist, point2))

    roid_dict_s = {k:sorted(v) for (k, v) in roid_dict.items()}

    roid_dict = {}
    for k in sorted(roid_dict_s):
        if k >= 270:
            roid_dict[k] = roid_dict_s[k]
    for k in sorted(roid_dict_s):
        if k < 270:
            roid_dict[k] = roid_dict_s[k]

    cnt = 1
    goal = 200
    while cnt < goal:
        for k in roid_dict:
            if not roid_dict[k]:
                continue
            print(f'#{cnt}  {k}° {roid_dict[k].pop(0)}')
            cnt += 1
            if cnt > goal:
                break


if __name__ == "__main__":
    main()
