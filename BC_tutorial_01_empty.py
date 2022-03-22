from multiprocessing.connection import wait
import cv2
from cv2 import imshow
from numpy import imag

print(cv2.__version__)

image = cv2.imread('images/logo.png', cv2.IMREAD_UNCHANGED)
imshow("image", image)

image_resized = cv2.resize(image, (100, 200), interpolation = cv2.INTER_AREA)
imshow("image_resized", image_resized)

image_rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
imshow("image_rotated", image_rotated)

path = "images/testimage.png"
cv2.imwrite(path, image_rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
