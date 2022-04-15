from scipy.io import wavfile
import sounddevice as sd

import cv2
import numpy as np
from PIL import Image as im
import matplotlib.pyplot as plt


dtype = np.dtype('B')
try:
    with open("data_test1.rgb", "rb") as f:
        numpy_data = np.fromfile(f, dtype)

    # print(numpy_data.dtype)

    for j in range(0, 9000):
        array1 = []
        for i in range(0, 480*270):
            index = 480*270*3*j
            array1.append([numpy_data[i+index], numpy_data[i+(480*270)+index], numpy_data[i+(480*270*2)+index]])

        array = np.array(array1)
        array2 = np.reshape(array, (270, 480, 3))
        # print(array2.dtype)

        # plt.imsave('demo2.png', array2)
        data = im.fromarray(array2).convert('RGB')
        data.save('images/{}.png'.format(j+1))

except IOError:
    print('Error While Opening the file!')

# samplerate, data = wavfile.read('data_test1.wav')
# sd.play(data, blocking=True)







