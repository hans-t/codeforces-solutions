# http://codeforces.com/problemset/problem/50/A
from sys import stdin, stdout

def read_int_input():
    return map(int, stdin.readline().rstrip().split())


def read_str_input():
    return stdin.readline().rstrip().split()


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    m, n = read_int_input()
    write_output(m*n//2)


main()
