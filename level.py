"""This file governs levels, reading and writing them from files, and
drawing them on the screen. The file format for a level is
12 bytes for the width, then 12 bytes for the height, then
12 bytes representing the tile each time."""
# TODO : might not want to handle drawing levels here.
# decouple drawing to its own file

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

    for i in range(0, len(level), 2):
        bytes = encode_12(level[i], level[i + 1])
        file.write(b''.join(bytes))

    file.close()

def load(filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    level = []
    for i in range(0, len(data), 3):
        level.extend(decode_12([data[i + x].to_bytes(1, 'big') for x in range(3)]))

    return level

from tile import TILES
def draw(level, surf):
    # level[0] = width of level, in tiles
    # level[1] = height of level, in tiles
    # level[2:] = rest of the level data
    width = level[0]
    height = level[1]
    for row in range(width):
        for col in range(height):
            tile = TILES[level[2:][row * width + col % width]]
            if tile != 0:
                tile.draw(surf, (row * tile.width, col * tile.height))