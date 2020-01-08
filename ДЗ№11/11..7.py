import numpy as np
from PIL import Image

numLevels = 6
imageSize = 3 ** numLevels

img = np.empty([imageSize, imageSize, 3], dtype=np.uint8)
img.fill(0)
color = np.array([77, 0, 255], dtype=np.uint8)

for level in range(0, numLevels + 1):
    stepSize = 3 ** (numLevels - level)
    for x in range(0, 3 ** level):
        if x % 3 == 1:
            for y in range(0, 3 ** level):
                if y % 3 == 1:
                    img[y * stepSize:(y + 1) * stepSize, x * stepSize:(x + 1) * stepSize] = color

        outputFilename = "sierpinski.bmp"
        Image.fromarray(img).save(outputFilename)