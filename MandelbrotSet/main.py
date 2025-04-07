import os
from PIL import Image
import math
import colorsys


width = 1000
x = -0.65
y = 0
xRange = 3.4
aspectRatio = 4 / 3
precision = 500

height = round(width / aspectRatio)
yRange = xRange / aspectRatio
minX = x - xRange / 2
maxX = x + xRange / 2
minY = y - yRange / 2
maxY = y + yRange / 2


img = Image.new('RGB', (width, height), color = 'black')
pixels = img.load()


def logColor(distance, base, const, scale):
    color = -1 * math.log(distance, base)
    rgb = colorsys.hsv_to_rgb(const + scale * color,0.8,0.9)
    return tuple(round(i * 255) for i in rgb)


def powerColor(distance, exp, const, scale):
    color = distance**exp
    rgb = colorsys.hsv_to_rgb(const + scale * color,1 - 0.6 * color,0.9)
    return tuple(round(i * 255) for i in rgb)


for row in range(height):
    for col in range(width):
        x = minX + col * xRange / width
        y = maxY - row * yRange / height
        oldX = x
        oldY = y

        for i in range(precision + 1):
            a = x**2 - y**2
            b = 2 * x * y
            x = a + oldX
            y = b + oldY
            if x**2 + y**2 > 4:
                break
            if i < precision:
                distance = (i + 1) / (precision  + 1)
                rgb = powerColor(distance, 0.2, 0.27, 1.0)
                pixels[col, row] = rgb

img.save('output.png')
os.system('open output.png')