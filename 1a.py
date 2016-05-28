from sys import stdin, stdout
from math import ceil


n, m, a = map(int, stdin.readline().rstrip().split())
res = ceil(n/a) * ceil(m / a)
stdout.write(str(res) + '\n')
