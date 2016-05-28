from sys import stdin, stdout


def read_int_input():
    return map(int, stdin.readline().rstrip().split())


def read_str_input():
    return stdin.readline().rstrip().split()


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    ...


main()
