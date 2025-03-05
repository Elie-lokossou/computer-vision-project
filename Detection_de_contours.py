#Programme de détection de contours avec OpenCV
import cv2

image = cv2.imread("Moto1.jpg")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

detecteur = cv2.Canny(gray,50,150)

cv2.imshow("Image Originale", image)
cv2.imshow("Contour détectés", detecteur)
cv2.waitKey(0)
cv2.destroyAllWindows()