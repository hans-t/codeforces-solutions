# http://codeforces.com/problemset/problem/118/A
from sys import stdin, stdout


def read_str_input():
    return stdin.readline().rstrip().split()


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    from functools import reduce
    word, = read_str_input()
    vowels = {'a', 'o', 'y', 'e', 'u', 'i'}
    lower_cased = map(lambda x: x.lower(), word)
    consonants = filter(lambda x: x not in vowels, lower_cased)
    result = reduce(lambda acc, curr: acc + '.' + curr, consonants, '')
    write_output(result)


main()
