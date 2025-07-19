#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

import hashlib


def main():
    msg = input('Input open key: ').strip() + 'sometext'
    print('Your password: ', int(sha256(msg)[0:6], 16))


def sha256(mess):
    m = hashlib.sha256()
    m.update(bytes(mess, 'utf-8'))
    return (m.hexdigest())


if __name__ == '__main__':
    main()
