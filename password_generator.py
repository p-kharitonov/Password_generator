from random import choices


def password_generator(length: int) -> str:
    array_symbols = ['abcdefghijkmnpqrstuvwxyz', 'ABCDEFGHJKLMNPQRSTUVWXYZ', '23456789', '#$%&*+-<=>?@_']
    while True:
        password = ''.join(choices(''.join(array_symbols), k=length))
        for symbols in array_symbols:
            for char in password:
                if char in symbols:
                    break
            else:
                break
        return password
