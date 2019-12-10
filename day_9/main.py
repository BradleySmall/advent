def get_input():
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

    o1, o2, o3 = 0, 0, 0
    if op in (1, 2, 7, 8):
        o3 = 1
    if op in (3,):
        o1 = 1

    return (h, k, t), (o1, o2, o3), op


def get_next_command(ip, rb, codes):
    parm_counts = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}
    modes, io, op = get_opcode(codes[ip])

    params = [0, 0, 0]
    ip += 1
    for x in range(parm_counts[op]):
        if io[x] == 1:                                  # output parameter
            if modes[x] == 0:                           # position mode
                params[x] = codes[ip] 
            elif modes[x] == 2:                         # relative mode
                params[x] = codes[ip]+rb
            else:
                print("Bad parameter mode for output")
        elif io[x] == 0:                                # input parameter
            if modes[x] == 0:                           # position mode
                params[x] = codes[codes[ip]] 
            elif modes[x] == 1:                         # immediate mode
                params[x] = codes[ip] 
            elif modes[x] == 2:                         # relative mode
                params[x] = codes[codes[ip]+rb] 
        ip += 1

    return ip, op, params


def exec_command(ip, op, rb, params, codes, inputs, outputs):
    if op == 1:  # add
        codes[params[2]] = params[0] + params[1]
    elif op == 2:  # multiply
        codes[params[2]] = params[0] * params[1]
    elif op == 3:  # inout
        # val = int(input("Enter input val? "))
        val = inputs.pop(0)
        codes[params[0]] = val
        # print(f"Input value = ({val})")
    elif op == 4:  # output
        # print(f"Output value = ({params[0]})")
        outputs.append(params[0])
    elif op == 5:  # branch true
        if params[0] != 0:
            ip = params[1]
    elif op == 6:  # branch false
        if params[0] == 0:
            ip = params[1]
    elif op == 7:  # less than
        if params[0] < params[1]:
            codes[params[2]] = 1
        else:
            codes[params[2]] = 0
    elif op == 8:  # equals
        if params[0] == params[1]:
            codes[params[2]] = 1
        else:
            codes[params[2]] = 0
    elif op == 9:  # adjust base address
        rb += params[0] 
    elif op == 99:  # halt
        # outputs.append(-1)
        ip = -1
    else:
        print('Bad Op Code ', op)
        ip = -1

    return ip, rb


def main():
    """Drive the program."""
    codes = get_input()
    codes.extend([0]*3000)
    ip = 0
    rb = 0
    params = []
    op = 0
    inputs = [2]
    outputs = []

    while ip != -1:
        ip, op, params = get_next_command(ip, rb, codes)
        ip, rb = exec_command(ip, op, rb, params, codes, inputs, outputs)

    print(outputs)

if __name__ == "__main__":
    main()


