from sys import stdin, stdout


def read_int_input():
    return map(int, stdin.readline().rstrip().split())


def read_str_input():
    return stdin.readline().rstrip().split()


def write_output(result):
    return stdout.write(str(result) + '\n')


def main():
    n, = read_int_input()
    for i in range(n):
        word, = read_str_input()
        word_length = len(word)
        if word_length > 10:
            new_word = word[0] + str(word_length - 2) + word[-1]
        else:
            new_word = word
        write_output(new_word)


main()
