import numpy as np
import cv2

def decrease_brightness(image, factor):
    # 轉換影像為浮點數型別
    image_float = image.astype(np.float32)
    
    # 降低亮度
    darkened_image = image_float - factor
    
    # 將值限制在0到255之間
    darkened_image = np.clip(darkened_image, 0, 255)
    
    # 將影像轉換為無符號8位整數型別
    darkened_image = darkened_image.astype(np.uint8)
    
    return darkened_image

img1 = cv2.imread("over_exposure_grey.jpg", -1)

# 降低亮度因子
brightness_factor = 50

# 將亮度降低
img2 = decrease_brightness(img1, brightness_factor)

cv2.imshow("Original Image", img1)
cv2.imshow("Your enhancement result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
