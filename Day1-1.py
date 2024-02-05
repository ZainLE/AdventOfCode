with open("day1.input", "r") as f:
    puzzle_input = f.read()

def part1(puzzle_input):
    total = 0

    for line in puzzle_input.split('\n'):
        digits = [c for c in line if c.isnumeric()]
        total += int(digits[0] + digits[-1])

    return total

print('Part 1:', part1(puzzle_input))