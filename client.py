#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

from server import sha256


def main():
    SALT = 'sometext'
    SECURE_KEY = input('Input open key: ').strip() + SALT
    PASSW = int(sha256(SECURE_KEY)[0:6], 16)
    print('Your password: {}'.format(PASSW))


if __name__ == '__main__':
    main()
