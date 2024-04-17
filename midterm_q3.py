import cv2

# 讀取影像
img = cv2.imread("carshort_grey.jpg", cv2.IMREAD_GRAYSCALE)

# 創建CLAHE對象
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# 對影像進行CLAHE處理
enhanced_img = clahe.apply(img)

# 顯示原始影像與增強後的影像
cv2.imshow("Original Image", img)
cv2.imshow("Enhanced Image (CLAHE)", enhanced_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
