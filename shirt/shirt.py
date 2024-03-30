import sys
from PIL import Image, ImageOps
import os

try:
    if len(sys.argv) > 3:
        raise IndexError
    arg1 = os.path.splitext(sys.argv[1])
    arg2 = os.path.splitext(sys.argv[2])
    if arg1[1] != arg2[1]:
        raise FileNotFoundError


    original = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    size = shirt.size
    cropped = ImageOps.fit(original, size)
    cropped.paste(shirt, shirt)
    cropped.save(sys.argv[2])


except:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if (arg1[1] != "png" or arg1[1] != "jpg" or arg1[1] != "jpeg") or (arg2[1] != "png" or arg2[1] != "jpg" or arg2[1] != "jpeg"):
        sys.exit("Invalid input")
    if arg1[1] != arg2[1]:
        sys.exit("Input and output have different extensions")





