from sys import stdin, stdout


def read_int_input():
    return map(int, stdin.readline().rstrip().split())


def read_str_input():
    return stdin.readline().rstrip().split()


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    n, = read_int_input()
    x = 0
    for _ in range(n):
        statement, = read_str_input()
        if '++' in statement:
            x += 1
        elif '--' in statement:
            x -= 1
    write_output(result=x)


main()
