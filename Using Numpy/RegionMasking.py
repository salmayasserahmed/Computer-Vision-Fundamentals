import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#1. Read The Image
image = mpimg.imread('test.jpg')
print("This image: ", type(image), "with dimensions ", image.shape)

#2. Make a Copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
region_select = np.copy(image)

#3. Decide the triangle region of interest | Take Care: (x=0,y=0) at the upper left in image processing
left_bottom =[0,539]
right_bottom = [900,300]
apex = [400,0]

#4. Identify the three sided region of interest (y=Ax+B) and the function np.polyfit returns that coefficients [A,B] of the fit
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]),(right_bottom[1],apex[1]),1)
fit_bottom = np.polyfit((right_bottom[0],left_bottom[0]),(left_bottom[1],right_bottom[1]),1)

#5. Find The Region Inside the Lines / np.meshgrid is inspired from MATLAB its a 2D Grid
XX, YY = np.meshgrid(np.arange(0,xsize),np.arange(0,ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
region_select[region_thresholds]=[255,0,0] #Red Color Pixels inside the region of interest
plt.imshow(region_select)
plt.show()