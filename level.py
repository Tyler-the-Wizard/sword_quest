"""This file governs levels, reading and writing them from files, and
drawing them on the screen. The file format for a level is
12 bytes for the width, then 12 bytes for the height, then
12 bytes representing the tile each time."""

#import sprite

def encode_12(num1, num2):
    """Encodes two 12-bit numbers as three 8-bit numbers
    and returns them as a byte array"""
    return [x.to_bytes(1, byteorder="big") for x in
        [num1 >> 4, ((num1 & 15) << 4) | (num2 >> 8), num2 & 255]]

def decode_12(bytes):
    """Decodes three 8-bit numbers in a byte
    array into two 12-bit numbers"""
    n = [int.from_bytes(x, "big") for x in bytes]
    return (n[0] << 4) | ((n[1] >> 4) & 15), ((n[1] & 15) << 8) | n[2]

def save(filename, level):
    file = open(filename, "wb")
    for byte in level:
        file.write(byte.to_bytes(1, byteorder='big'))

    file.close()

def load(filename):
    file = open(filename, "rb")

    file.close()

def draw(level, screen):
    pass

# test code
save("test.lv", [48, 49, 50, 51, 52, 53])