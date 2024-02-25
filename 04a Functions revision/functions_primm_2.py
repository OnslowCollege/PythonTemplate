"""
functions_primm_2.py.

Created by: Arkin E
Date: 26.02.2024
"""

def get_image_bits(width: int, height: int, depth: int):
    pixels = width * height
    bit_count = pixels * depth
    print(bit_count)




get_image_bits(100, 200, 32)