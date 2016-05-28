# http://codeforces.com/problemset/problem/158/A
from sys import stdin, stdout


def read_int_input():
    return map(int, stdin.readline().rstrip().split())


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    n, k = read_int_input()
    scores = tuple(read_int_input())
    score_k = scores[k-1]
    count = k
    if score_k:
        for score in scores[k:]:
            if score == score_k:
                count += 1
            else:
                break
    else:
        for score in reversed(scores[:k]):
            if score:
                break
            else:
                count -= 1
    write_output(count)


main()
