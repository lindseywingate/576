import cv2
import numpy as np
import glob


img_array = []
for i in range(9000):
    img = cv2.imread('images/{}.png'.format(i+1))
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

# print(img_array)
# print(size)

out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(9000):
    out.write(img_array[i])

out.release()
