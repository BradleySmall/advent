"""1202 Program Alarm."""
import itertools


def get_codes():
    with open('input.txt') as f:
        return [int(num) for num in f.readline().strip().split(',')]


def get_opcode(opcode):
    tmp = int(opcode)
    op = tmp % 100
    tmp //= 100
    h = tmp % 10
    tmp //= 10
    k = tmp % 10
    tmp //= 10
    t = tmp % 10

    return h, k, t, op


def get_opcode2(opcode):
    tmp = int(opcode)
    op = tmp % 100
    tmp //= 100
    h = tmp % 10
    tmp //= 10
    k = tmp % 10
    tmp //= 10
    t = tmp % 10

    if op in (1, 2, 7, 8):
        t = 1
    if op in (3,):
        h = 1

    return (h, k, t), op


def op_get_size(op):
    if op == 1:
        return 4
    if op == 2:
        return 4
    if op == 3:
        return 2
    if op == 4:
        return 2
    if op == 5:
        return 3
    if op == 6:
        return 3
    if op == 7:
        return 4
    if op == 8:
        return 4
    if op == 99:
        return 1


def get_next_command(ip, codes):
    parm_counts = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0}
    modes, op = get_opcode2(codes[ip])

    params = [0,0,0]
    ip += 1
    for x in range(parm_counts[op]):
        params[x] = codes[ip]
        if modes[x] == 0:
            params[x] = codes[params[x]]
        ip += 1


    return ip, op, params


def exec_command(ip, op, params, codes):
    if op == 1:
        codes[params[2]] = params[0] + params[1]
    elif op == 2:
        codes[params[2]] = params[0] * params[1]
    elif op == 3:
        val = int(input('Enter input val? '))
        codes[params[0]] = val
    elif op == 4:
        print(f'Output value = ({params[0]})')
    elif op == 5:
        if params[0] != 0:
            ip = params[1]
    elif op == 6:
        if params[0] == 0:
            ip = params[1]
    elif op == 7:
        if params[0] < params[1]:
            params[2] = 1
    elif op == 8:
        if params[0] == params[1]:
            params[2] = 1
        else:
            params[2] = 0
    elif op == 99:
        ip = -1
    else:
        print(f'Bad Op Code {op}')
        ip = -1

    return ip


def run_program(codes):
    ip = 0
    while ip != -1:
        ip, op, params = get_next_command(ip, codes)
        ip = exec_command(ip, op, params, codes)


def run_computer(codes):
    ip = 0
    while codes[ip] != 99:
        p1_mode, p2_mode, p3_mode, op = get_opcode(codes[ip+0])
        # print(p1_mode, p2_mode, p3_mode, op)
        size = op_get_size(op)
        if size == 1:
            pass

        parm1 = codes[ip+1]
        outpt = parm1
        if p1_mode == 0:
            parm1 = codes[parm1]

        if size == 4:
            parm2 = codes[ip+2]
            if p2_mode == 0:
                parm2 = codes[parm2]

            outpt = codes[ip+3]

        if op == 1:
            codes[outpt] = parm1 + parm2
        elif op == 2:
            codes[outpt] = parm1 * parm2
        elif op == 3:
            val = int(input('Enter input val? '))
            codes[outpt] = val
        elif op == 4:
            print(f'Output value = ({parm1})')
        else:
            print(f'Bad Op Code {op}')
            break
        ip += size


def main2():
    """Drive the program."""
    codes = get_codes()

    new_codes = [code for code in codes]

    run_computer(new_codes)


def main():
    """Drive the program."""
    codes = get_codes()

    run_program(codes)


if __name__ == "__main__":
    main()
