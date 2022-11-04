import random
import string
import itertools

def main():
    code = ''
    code_list = list(itertools.chain(string.digits, string.ascii_letters))
    print(code_list)
    for i in range(4):
        choice = random.choice(code_list)
        code += choice
    print(code)


if __name__ == '__main__':
    main()
    ...