"""Day 3: Crossed Wires."""


def get_paths():
    """Read in the path information."""
    with open('input.txt') as f:
        return [path.rstrip('\n').split(',') for path in f.readlines()]


def path_to_pairs(cur, path):
    """Convert path into list of pairs."""
    direction = path[0]
    extent = int(path[1:])

    pairs = []
    for _ in range(extent):
        if direction == 'L':
            cur[0] -= 1
        elif direction == 'R':
            cur[0] += 1
        elif direction == 'U':
            cur[1] += 1
        elif direction == 'D':
            cur[1] -= 1
        pairs.append((cur[0], cur[1]))
    return pairs


def main():
    """Drive the main program."""
    paths = get_paths()

    pairs1 = []
    pairs2 = []

    cur = [0, 0]
    for i in paths[0]:
        pairs1.extend(path_to_pairs(cur, i))

    cur = [0, 0]
    for i in paths[1]:
        pairs2.extend(path_to_pairs(cur, i))

    intr = set(pairs1).intersection(set(pairs2))
    dist1 = [(abs(a) + abs(b), (a, b)) for a, b in intr]
    dist2 = [(1 + pairs1.index((a, b)) + 1 + pairs2.index((a, b)), (a, b))
             for a, b in intr]
    print(min(dist1))
    print(min(dist2))


if __name__ == "__main__":
    main()
