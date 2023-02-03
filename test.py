import numpy as np
from delete_this import *

color_data_HSV = []

a, b = map(int, input().split())
color_data_RGB = input().split(" ")
print("input info:")
print(f"Picture size == {a, b}")
print(color_data_RGB)
print("/////////////////")


for indx, color in enumerate(color_data_RGB):
    rr = int(color[:2], 16)
    gg = int(color[2:4], 16)
    bb = int(color[:4], 16)
    data_conv = rgb_to_hsv(np.array([rr, gg, bb])

    print(data_conv)



