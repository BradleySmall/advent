"""Day 7: Amplification Circuit."""

from itertools import permutations

def get_codes():
    with open("input.txt") as f:
        return [int(num) for num in f.readline().strip().split(",")]


def get_opcode(opcode):
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


def get_next_command(ip, codes):
    parm_counts = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}
    modes, op = get_opcode(codes[ip])

    params = [0, 0, 0]
    ip += 1
    for x in range(parm_counts[op]):
        params[x] = codes[ip]
        if modes[x] == 0:
            params[x] = codes[params[x]]
        ip += 1

    return ip, op, params


def exec_command(ip, op, params, codes, inputs, output):
    if op == 1:                            # add
        codes[params[2]] = params[0] + params[1]
    elif op == 2:                          # multiply
        codes[params[2]] = params[0] * params[1]
    elif op == 3:                          # inout
        # val = int(input("Enter input val? "))
        val = inputs.pop(0)
        codes[params[0]] = val
    elif op == 4:                          # output
        # print(f"Output value = ({params[0]})")
        output = params[0]
    elif op == 5:                          # branch true
        if params[0] != 0:
            ip = params[1]
    elif op == 6:                          # branch false
        if params[0] == 0:
            ip = params[1]
    elif op == 7:                          # less than
        if params[0] < params[1]:
            codes[params[2]] = 1
        else:
            codes[params[2]] = 0
    elif op == 8:                          # equals
        if params[0] == params[1]:
            codes[params[2]] = 1
        else:
            codes[params[2]] = 0
    elif op == 99:                         # halt
        ip = -1
    else:
        print(f"Bad Op Code {op}")
        ip = -1

    return ip, output


def run_program(codes, inputs, output):
    ip = 0
    while ip != -1:
        ip, op, params = get_next_command(ip, codes)
        ip, output = exec_command(ip, op, params, codes, inputs, output)
    return output

def main():
    """Drive the program."""
    inputs = list(permutations(range(5)))

    # inputs = [(2,0,3, 0, 1,0,0,0,4,0)]
    # print (inputs[:10])
    # return
    max = -1
    sig = []
    seq = []
    for series in inputs:
        output = 0
        l = iter(series)
        out = []
        for _ in range(5):
            codes = get_codes()
            output = run_program(codes, [next(l), output], output)

        if output > max:
            max = output
            sig = series
            seq = output
    print(f'Max({max}), Signal({sig}) Out({seq})')

if __name__ == "__main__":
    main()
