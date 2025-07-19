#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

from server import sha256


def main():
    SECURE_PHRASE = 'sometext'
    SECURE_KEY = input('Input open key: ').strip() + SECURE_PHRASE

    print('Your password: ', int(sha256(SECURE_KEY)[0:6], 16))


if __name__ == '__main__':
    main()
