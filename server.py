#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

import time
import qrcode
import hashlib


def main():
    SALT = 'sometext'

    rnd_phrase = str(time.time()) + SALT

    OPEN_KEY = sha256(rnd_phrase)
    SECURE_KEY = OPEN_KEY + SALT
    PASSW = int(sha256(SECURE_KEY)[0:6], 16)

    qr_gen(OPEN_KEY)
    print('Open key: {}'.format(OPEN_KEY))
    if int(input("Input password: ")) == PASSW:
        print('succes')
    else:
        print('fail')


def qr_gen(data):
    img = qrcode.make(data)
    img.save("qr.png")
    print("QR-code save as <qr.png>")


def sha256(data) -> str:
    hsh = hashlib.sha256()
    hsh.update(bytes(data, 'utf-8'))
    return hsh.hexdigest()


if __name__ == '__main__':
    main()
