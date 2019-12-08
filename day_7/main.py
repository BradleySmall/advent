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


def exec_command(ip, op, params, codes, inputs, outputs):
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
    elif op == 99:  # halt
        outputs.append(-1)
        ip = -1
    else:
        print(f"Bad Op Code {op}")
        ip = -1

    return ip


class Amp:
    def __init__(self):
        self.codes = get_codes()
        self.ip = 0

    def run(self, inputs):
        while self.ip != -1:
            self.ip, op, params = get_next_command(self.ip, self.codes)
            outputs = []
            self.ip = exec_command(self.ip, op, params, self.codes, inputs, outputs)
            if len(outputs):
                return outputs[0]


def main():
    """Drive the program."""
    inputs = list(permutations(range(5, 10)))

    signal = -1
    l_series = None
    for series in inputs:

        amp_a = Amp()
        amp_b = Amp()
        amp_c = Amp()
        amp_d = Amp()
        amp_e = Amp()

        output = amp_a.run([series[0], 0])
        output = amp_b.run([series[1], output])
        output = amp_c.run([series[2], output])
        output = amp_d.run([series[3], output])
        output = amp_e.run([series[4], output])

        largest = 0
        while output != -1:
            output = amp_a.run([output])
            output = amp_b.run([output])
            output = amp_c.run([output])
            output = amp_d.run([output])
            output = amp_e.run([output])
            if output != -1:
                largest = output
        if largest > signal:
            signal = largest
            l_series = series
    print(signal, l_series)


if __name__ == "__main__":
    main()
