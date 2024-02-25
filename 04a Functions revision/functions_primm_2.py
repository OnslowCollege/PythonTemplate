"""
functions_primm_2.py.

Created by: Arkin E
Date: 26.02.2024
"""

def get_image_bits(width: int, height: int, depth: int = 32) -> int:
    """
    Calculates the required storage size of an uncompressed image.
    And returns bit count
    
    width - The width of the image in pixels.
    height - The height of the image in pixels.
    depth - The bit depth of the image, or the number of bits per pixel.
    bit count - pixels * depth
    """

    pixels = width * height
    return pixels * depth




bit_count = get_image_bits(100, 200, 32)
print(bit_count)