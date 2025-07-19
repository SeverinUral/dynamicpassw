#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

import time
import hashlib


def main():
    mess = str(time.time()) + 'UNONA'
    old = sha256(mess)
    new = str(old) + 'sometext'
    print(old)
    dig = int(sha256(new)[0:6], 16)

    if int(input()) == dig:
        print('succes')
    else:
        print('fail')


def sha256(mess):
    m = hashlib.sha256()
    m.update(bytes(mess, 'utf-8'))
    return (str(m.hexdigest()))


if __name__ == '__main__':
    main()
