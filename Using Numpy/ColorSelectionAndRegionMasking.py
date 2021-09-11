import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#1. Read The Image
image = mpimg.imread('test.jpg')

#2. Print out some stats
print("This image: ", type(image),
      "with dimensions", image.shape)

#3. Copy x and y of the image to work on it
ysize = image.shape[0]
xsize = image.shape[1]

#4. Copy the image for color selection and region masking
color_selection = np.copy(image)
region_selection = np.copy(image)

#5. Set the variables of threshold for RGB image
red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold=[red_threshold,green_threshold,blue_threshold]

#6. Define region of interest of the triangle
left_bottom = [156,536]
right_bottom = [789,532]
apex = [475,320]

#7. Identify the three sided region of interest
fit_left = np.polyfit((left_bottom[0],apex[0]),(left_bottom[1],apex[1]),1)
fit_right = np.polyfit((right_bottom[0],apex[0]), (right_bottom[1],apex[1]),1)
fit_bottom = np.polyfit((right_bottom[0],left_bottom[0]),(left_bottom[0],right_bottom[1]),1)

#8. Mask the pixels below the threshold
color_thresholds = (image[:,:,0] < rgb_threshold[0]) | \
                    (image[:,:,1] < rgb_threshold[1]) | \
                    (image[:,:,2] < rgb_threshold[2])
#9. Find the region inside lines
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
#10. Mask the color selection
#color_selection[color_thresholds] = [0,0,0]
#11. Find both the image is in the region and colored right
# Mask color and region selection
color_selection[color_thresholds | ~region_thresholds] = [0, 0, 0]
# Color pixels red where both color and region selections met
region_selection[~color_thresholds & region_thresholds] = [255, 0, 0]

# Display the image and show region and color selections
plt.imshow(image)
x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]
plt.plot(x, y, 'b--', lw=4)
plt.imshow(color_selection)
plt.imshow(region_selection)
plt.show()