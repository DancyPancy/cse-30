import numpy as np
import cv2
import matplotlib.image as mimg

file = 'redbox.jpg'

im_arr = np.array([[[0, 0, 255], [255, 0, 0]], [[0, 255, 0], [255, 255, 255]]])

def mod_img(im_arr, binary):
    new_im_arr = im_arr.copy()
    bit_id = 0
    # iterates through the pixels of an array and modifies the values with the encoded message
    for i, pix in np.ndenumerate(im_arr):
        if bit_id >= len(binary):
            break
        new_im_arr[i[0]][i[1]][i[2]] += int(binary[bit_id]) - (pix % 2)
        bit_id += 1

    return new_im_arr


test = int('test')