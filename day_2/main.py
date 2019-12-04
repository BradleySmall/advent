"""1202 Program Alarm."""
import itertools


def get_codes():
    with open('input.txt') as f:
        return [int(num) for num in f.readline().strip().split(',')]


def run_computer(codes):
    ip = 0
    while codes[ip] != 99:
        op = codes[ip+0]
        parm1 = codes[ip+1]
        parm2 = codes[ip+2]
        outpt = codes[ip+3]
        if op == 1:
            codes[outpt] = codes[parm1] + codes[parm2]
        elif op == 2:
            codes[outpt] = codes[parm1] * codes[parm2]
        else:
            print('Bad Op Code')
            break
        ip += 4


def main():
    """Drive the program."""
    codes = get_codes()

    new_codes = [code for code in codes]
    new_codes[1] = 12
    new_codes[2] = 2
    run_computer(new_codes)

    goal = 19690720
    for parm1, parm2 in itertools.product(range(100), range(100)):
        new_codes = [code for code in codes]
        new_codes[1] = parm1
        new_codes[2] = parm2
        run_computer(new_codes)
        if new_codes[0] == goal:
            break
    else:
        print("{goal} not found")

    print(f'noun = {parm1}, verb = {parm2} answer = {100 * parm1 + parm2}')


if __name__ == "__main__":
    main()
