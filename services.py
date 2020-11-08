import pdb


def compute_lcm(x, y):
    x = int(x)
    y = int(y)
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


def sort_numbers(numbers):
    for i, n in enumerate(numbers):
        numbers[i] = int(n.strip("\r"))
    sorted_numbers = sorted(numbers)
    return sorted_numbers
