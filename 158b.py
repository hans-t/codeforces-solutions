from sys import stdin, stdout


def read_int_input():
    return map(int, stdin.readline().rstrip().split())


def read_str_input():
    return stdin.readline().rstrip().split()


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    from math import ceil

    n, = read_int_input()
    sequence = tuple(read_int_input())

    # why does it work?

    counter = {i: 0 for i in range(1, 5)}
    for size in sequence:
        counter[size] += 1

    # Add all fours.
    taxi_count = counter.pop(4)
    threes = counter.pop(3)
    twos = counter.pop(2)
    ones = counter.pop(1)

    # no other group can complement threes except ones, so add number of threes to taxi count.
    taxi_count += threes
    if ones > threes:
        ones -= threes
    else:
        ones = 0
    threes = 0

    # 2's can only be complemented by 1's.
    # there is either a 2-group left or none.
    taxi_count += (twos // 2)

    # if there are ones left, put two 1's inside a taxi that has one group of 2, or
    # in a new taxi. In either case we need one more taxi.
    twos %= 2
    if twos and ones >= 2:
        taxi_count += 1
        twos = 0
        ones -= 2

    taxi_count += ceil((twos + ones) / 4)
    write_output(taxi_count)
main()
