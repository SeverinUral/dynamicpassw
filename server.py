#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2025 Fomenko A V

import time
import hashlib

import qrcode
from qrcode.image.pure import PyPNGImage

SALT = "sometext"


def main():
    NUMBER_OF_TRIES = 5
    OPEN_KEY = sha256(str(time.time()) + SALT)
    SECURE_KEY = OPEN_KEY + SALT
    PASSW = int(sha256(SECURE_KEY)[0:6], 16)

    qr_gen(OPEN_KEY)
    print(f"Open key: {OPEN_KEY}")
    while NUMBER_OF_TRIES:
        if int(input("Input password: ")) == PASSW:
            print("succes")
            return
        else:
            print("fail\ntry again...")
            NUMBER_OF_TRIES -= 1


def qr_gen(data):
    qr = qrcode.QRCode()
    qr.add_data(data)

    qr.print_ascii()

    img = qr.make_image(image_factory=PyPNGImage)
    img.save("qr.png")


def sha256(data) -> str:
    hsh = hashlib.sha256()
    hsh.update(bytes(data, "utf-8"))
    return hsh.hexdigest()


if __name__ == "__main__":
    main()
