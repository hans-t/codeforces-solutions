# http://codeforces.com/problemset/problem/1/A
from sys import stdin, stdout


def read_int_input():
    return map(int, stdin.readline().rstrip().split())


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    from math import ceil
    n, m, a = read_int_input()
    result = ceil(n/a) * ceil(m / a)
    write_output(result)


main()
