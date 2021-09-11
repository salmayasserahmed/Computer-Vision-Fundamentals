import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#To use canny edge detection
import cv2
#1. Read The Image
image = mpimg.imread("TobeCanny.jpg")

#2. Convert into greyscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #Gray Conversion
plt.imshow(gray, cmap='gray') #Cmap controls the colour map used to display the value when and image have only (M,N)


#4. Define Kernel Size for Gaussian smoothing or blurring [Optional Step]
kernal_size = 5 #Must be an Odd Number
blur_gray = cv2.GaussianBlur(gray,(kernal_size,kernal_size),0)

#5. Define low and high threshold to run Canny
low_threshold = 50
high_threshold = 300

#6. Apply Canny
edge = cv2.Canny(gray,low_threshold, high_threshold)
plt.imshow(edge, cmap='Greys_r')
plt.show()
