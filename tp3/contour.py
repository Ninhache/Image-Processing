import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sympy import im

from mask import robert3d, prewitt, sobel, laplacien1, laplacien2


tmpImage = cv.imread("canvas.png")


def convolution2D(image, filtre):
    shape = np.shape(image) # (256, 256)
    imageConvolue = np.zeros(shape) # (256, 256) filled with 0 

    c = (filtre.shape[0]-1) // 2 
    l = (filtre.shape[1]-1) // 2 

    for j in range(l, (image.shape[1] - l)): # 1:255
        for i in range(c, (image.shape[0] - c)): # 0:255
            imageConvolue[i,j] = np.sum(image[i - c : i + c + 1, j - l : j + l + 1] * filtre)

    return imageConvolue

def imgContourGRAD(image, filtre, seuil = 100):
    gx = convolution2D(image, filtre)
    gy = convolution2D(image, np.rot90(filtre))
    module = np.sqrt(gx * gx + gy * gy)

    ret, contour = cv.threshold(module, seuil, 255, cv.THRESH_BINARY)

    return contour

def imgContourLAPLAC(image, filtre, seuil = 100):
    laplace = convolution2D(image, filtre)

    shape = np.shape(image) # (256, 256)
    imageRes = np.zeros(shape) # (256, 256) filled with 0 

    t = 3 // 2
    
    for j in range(t, (image.shape[1] - t)):
        for i in range(t, (image.shape[0] - t)):
            matrix = image[i - t : i + t + 1, j - t : j + t + 1]
            minValue = np.amin(matrix)
            maxValue = np.amax(matrix)
            moyValue = maxValue - minValue
            
            if(maxValue > 0 and minValue < 0 and moyValue > seuil):
                imageRes[i, j] = 1
            else:
                imageRes[i, j] = 0

    return imageRes

def openImageInWindow(image1):
    plt.figure("title")
    
    plt.subplot(1,1,1)
    plt.imshow(image1)    

    plt.show()


def openImagesInWindow(image1, image2, image3):
    plt.figure("title")
    
    plt.subplot(1,3,1)
    plt.imshow(image1)
    

    plt.subplot(1,3,2)
    plt.imshow(image2)
    

    plt.subplot(1,3,3)
    plt.imshow(image3)
    

    plt.show()


tmpSeuil = 50
'''
imgRobert   = imgContourGRAD(tmpImage, robert3d, tmpSeuil)
imgPrewitt  = imgContourGRAD(tmpImage, prewitt, tmpSeuil)
imgSobel    = imgContourGRAD(tmpImage, sobel, tmpSeuil)

openImagesInWindow(imgRobert, imgPrewitt, imgSobel)
'''
imgLaplace1 = imgContourLAPLAC(tmpImage, laplacien1)
openImageInWindow(imgLaplace1)