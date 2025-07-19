#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

import hashlib


def main():
    old = input()
    new = old + 'sometext'
    print(int(sha256(new)[0:6], 16))


def sha256(mess):
    m = hashlib.sha256()
    m.update(bytes(mess, 'utf-8'))
    return (str(m.hexdigest()))


if __name__ == '__main__':
    main()
