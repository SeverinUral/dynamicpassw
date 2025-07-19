#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

import time
import hashlib


def main():
    SECURE_PHRASE = 'sometext'

    rnd_phrase = str(time.time()) + SECURE_PHRASE

    OPEN_KEY = sha256(rnd_phrase)
    SECURE_KEY = OPEN_KEY + SECURE_PHRASE
    PASSW = int(sha256(SECURE_KEY)[0:6], 16)

    print('Open key: ', OPEN_KEY)
    if int(input("Input password: ")) == PASSW:
        print('succes')
    else:
        print('fail')


def sha256(data) -> str:
    hsh = hashlib.sha256()
    hsh.update(bytes(data, 'utf-8'))
    return hsh.hexdigest()


if __name__ == '__main__':
    main()
