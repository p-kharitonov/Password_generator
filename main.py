from password_generator import password_generator


def main():
    max_iteration = 10
    for _ in range(max_iteration):
        length = input('Enter password length (minimum is 8): ')
        if length.isdigit() and int(length) >= 8:
            print('Password:', password_generator(int(length)))
            break
        print('Invalid input!')
    else:
        print('Too much wrong input!')


if __name__ == '__main__':
    main()