import cv2

# TODO load images in grey and color
image_gray = cv2.imread('images/logo.png', cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread('images/logo.png', cv2.IMREAD_COLOR)

# TODO do some print out about the loaded data
print(type(image_gray))
print(type(image_color))

# TODO Continue with the color image or the grayscale image

image = image_gray.copy()

# TODO Extract the size or resolution of the image
height = image.shape[0]
width = image.shape[1]
print(height, width)

# TODO resize image

image = cv2.resize(image, (100, 100))

# TODO print first row

print(image[0,:])

# TODO print first column

print(image[:,0])

# TODO set an area of the image to black

image[40:60,40:60] = 0
cv2.imshow("image", image)

# TODO find all used colors in the image
height = image.shape[0]
width = image.shape[1]
colors = []
for i in range(height):
    for j in range(width):
        curr_color = image[i, j]
        if colors.count(curr_color) == 0:
            colors.append(curr_color)
print(colors)

# TODO copy one part of an image into another one

# TODO save image

# TODO show the image

# TODO show the original image (copy demo)

cv2.waitKey(0)
cv2.destroyAllWindows()
