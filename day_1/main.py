"""Day 1: The Tyranny of the Rocket Equation."""


def get_masses():
    """Read in the list of masses."""
    with open("input.txt") as f:
        return [int(line.rstrip('\n')) for line in f.readlines()]


def calc_module_fuel_req(mass):
    """Calculate the fuel requirements for mass + fuel."""
    total_fuel = 0

    fuel = (mass // 3) - 2
    while fuel > 0:
        total_fuel += fuel
        fuel = (fuel // 3) - 2
    return total_fuel


def main():
    """Drive the program."""
    masses = get_masses()

    total_fuel_req = 0
    for mass in masses:
        total_fuel_req += calc_module_fuel_req(mass)

    print(f'Total fuel required {total_fuel_req}')


if __name__ == "__main__":
    main()
