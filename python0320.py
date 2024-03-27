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
    img_adj = np.floor(img + 0.5)
    img_adj[img_adj > 255] = 255
    img_adj[img_adj < 0 ] = 0 
    return img_adj.astype(np.uint8)

def histogram( f ):
    if f.ndim != 3:
        hist = cv2.calcHist( [f], [0], None, [256], [0,256] )
        plt.plot( hist )
    else:
        color = ( 'b', 'g', 'r')
        for i, col in enumerate( color ):
            hist = cv2.calcHist( f, [i], None, [256], [0,256] )
    plt.xlim( [0,256] )
    plt.xlabel( "Intensity" )
    plt.ylabel( "#Intensities" )
    plt.show( )
    
img = cv2.imread( "..\dataset\Lena.pgm", -1 )
cv2.imshow( "Original Image", img.astype(np.uint8) )
print(f'In the original image, mean={img.mean()}, std={img.std()}')
histogram(img)

img_adj = adjust_image_by_offset(img, 150)

img_adj = adjust_image_by_offset(img, -150)

img_adj = adjust_image_by_scaling(img, scale=0.6)

img_adj = adjust_image_by_scaling(img, scale=1.3)


img_adj = adjust_image_by_offset(img, -img.mean())
print(f'In the adjusted image, mean={img_adj.mean()}, std={img_adj.std()}')
img_adj = adjust_image_by_scaling(img_adj , 0.5)
print(f'In the adjusted image, mean={img_adj.mean()}, std={img_adj.std()}')
img_adj = adjust_image_by_offset(img_adj, img.mean())
img_adj =  convert_image_to_unit8(img_adj)
cv2.imshow( "make standard deviation smaller", img_adj )
print(f'In the adjusted image, mean={img_adj.astype(np.uint8).mean()})




