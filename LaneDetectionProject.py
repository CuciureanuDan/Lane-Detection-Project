import matplotlib.pyplot as plt
import numpy as np
import skimage.io as io
from skimage.feature import canny

# include the path to your file #TDL add a tkinker option to select
imgFileName = "C:\\Users\\dancu\\OneDrive - Technical University of Cluj-Napoca\\Facultate\\PNIproject\\lane5.jpg"
image = io.imread(imgFileName, as_gray=True) # we read the image without color information


if image is None:
    print("Failed to get the image. check path")
else:
    edges = canny(image, sigma=2)#, low_threshold=0.1, high_threshold=0.5)

    fig, ax = plt.subplots(1,2, figsize=(12,6))

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title("Original Image")
    ax[0].axis('off')

    ax[1].imshow(edges, cmap='gray')
    ax[1].set_title("Canny Edge Detection")
    ax[1].axis('off')

    # plt.imshow(edges, cmap='gray')
    # plt.axis('off')
    # plt.show(block=True)

plt.show() # block=True

