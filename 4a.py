from sys import stdin, stdout


def read_int_input():
    return map(int, stdin.readline().rstrip().split())


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    w, = read_int_input()
    result = 'YES' if w % 2 == 0 and w > 2 else 'NO'
    write_output(result)



main()
