#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

import io
import time
import hashlib

import qrcode
from qrcode.image.pure import PyPNGImage


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
    f = io.StringIO()
    qr = qrcode.QRCode()
    qr.add_data(data)

    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())

    img = qr.make_image(image_factory=PyPNGImage)
    img.save("qr.png")
    print("QR-code save as <qr.png>")


def sha256(data) -> str:
    hsh = hashlib.sha256()
    hsh.update(bytes(data, 'utf-8'))
    return hsh.hexdigest()


if __name__ == '__main__':
    main()
