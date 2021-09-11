import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#1. Read the Image
image = mpimg.imread("test.jpg")

#2. Print out some stats
print("This image is: ", type(image), "with dimensions", image.shape)

#3. Grab x and y of the image and make a copy to work on it
ysize = image.shape[0]
xsize = image.shape[1]

#4. Make a Copy
color_select = np.copy(image)

#5. Define a color threshold for blue, green and red images
red_threshold = 200
green_threshold = 200
blue_threshold = 200



#6. A vector that contains the minimum value for RGC
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

#7. Identify Pixels Below Threshold
thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])
color_select[thresholds] = [0,0,0]
plt.imshow(color_select)
plt.show()

