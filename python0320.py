import numpy as np
import cv2
import matplotlib.pyplot as plt

def adjust_image_by_offset(img, offset=0):
    img_adj = img.astype(np.float16)
    img_adj = img_adj + offset
    return img_adj

def adjust_image_by_scaling(img, scale=1.0):
    img_adj = img.astype(np.float16)
    img_adj = img_adj * scale
    return img_adj

def convert_image_to_unit8(img):
    img_adj = np.floor(img_adj + 0.5)
    img_adj = np.floor(img_adj + 0.5)
    img_adj[img_adj > 255] = 255
    img_adj[img_adj < 0 ] = 0   