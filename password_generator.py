from random import choice


def generator(length):
    lowercase_letters = 'abcdefghijkmnpqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    digits = '23456789'
    special = '#$%&*+-<=>?@_'
    symbols = [lowercase_letters, uppercase_letters, digits, special]
    chars = ''.join(symbols)
    while True:
        password = ''
        for _ in range(length):
            password += choice(chars)
        for elem in symbols:
            if not any([char in elem for char in password]):
                break
        else:
            break
    return password


def main():
    while True:
        length = input('Enter password length (minimum is 8): ')
        if length.isdigit() and int(length) >= 8:
            length = int(length)
            break
        print('Invalid input!')
    print('Password:', generator(length))


if __name__ == '__main__':
    main()
