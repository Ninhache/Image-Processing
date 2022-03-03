import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sympy import im

from mask import robert3d, prewitt, sobel, laplacien1, laplacien2


tmpImage = cv.imread("canvas.png",0)


def convolution2D(image, filtre):
    shape = np.shape(image) # (256, 256)
    imageConvolue = np.zeros(shape) # (256, 256) filled with 0 

    c = (filtre.shape[0]-1) // 2 
    l = (filtre.shape[1]-1) // 2 

    for i in range(l, (image.shape[1] - l)): # 1:255
        for j in range(c, (image.shape[0] - c)): # 0:255
            imageConvolue[i,j] = np.sum(image[i - c : i + c + 1, j - l : j + l + 1] * filtre)

    return imageConvolue

def imgContourGRAD(image, filtre, seuil = 100):
    gx = convolution2D(image, filtre)
    gy = convolution2D(image, np.rot90(filtre))
    module = np.sqrt(gx * gx + gy * gy)

    ret, contour = cv.threshold(module, seuil, 255, cv.THRESH_BINARY)

    return contour

def imgContourLAPLAC(image, filtre, seuil):
    laplace = convolution2D(image, filtre)

    shape = np.shape(image) # (256, 256)
    imageRes = np.zeros(shape) # (256, 256) filled with 0 

    t = 3 // 2

    
    
    for heigth in range(t, (laplace.shape[1] - t )):
        for width in range(t, (laplace.shape[0] - t )):
            # 
            matrix = laplace[width - t : width + t + 1, heigth - t : heigth + t + 1]
        
            minValue = np.min(matrix)
            maxValue = np.max(matrix)
            moyValue = maxValue - minValue
            
            if(maxValue > 0 and minValue < 0 and moyValue > seuil):
                imageRes[width, heigth] = 1
            else:
                imageRes[width, heigth] = 0

    return imageRes,laplace

def openImageInWindow(image1):
    plt.figure("title")
    
    plt.subplot(1,1,1)
    plt.imshow(image1)    

    plt.show()


def openImagesInWindow(image1, image2):
    plt.figure("title")
    
    plt.subplot(1,2,1)
    plt.imshow(image1,'gray')
    

    plt.subplot(1,2,2)
    plt.imshow(image2,'gray')
    
    

    plt.show()



'''
imgRobert   = imgContourGRAD(tmpImage, robert3d, tmpSeuil)
imgPrewitt  = imgContourGRAD(tmpImage, prewitt, tmpSeuil)
imgSobel    = imgContourGRAD(tmpImage, sobel, tmpSeuil)

openImagesInWindow(imgRobert, imgPrewitt, imgSobel)
'''
#imgLaplace1 = cv.Laplacian(tmpImage, cv.CV_32F)

tmpSeuil = 100
imgLaplace1,l1 = imgContourLAPLAC(tmpImage, laplacien1, tmpSeuil)
imgLaplace2,l2 = imgContourLAPLAC(tmpImage, laplacien2, tmpSeuil)
print(np.min(imgLaplace2))

openImagesInWindow(imgLaplace1, imgLaplace2)