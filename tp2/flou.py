import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math as math

from sympy import im


cellules=cv.imread("canvas.png",0)

def convolution2D(image, filtre):
    shape = np.shape(image) # (256, 256)
    imageConvolue = np.zeros(shape) # (256, 256) filled with 0 

    c = (filtre.shape[0]-1) // 2 
    l = (filtre.shape[1]-1) // 2 

    for j in range(l, (image.shape[1] - l)): # 1:255
        for i in range(c, (image.shape[0] - c)): # 0:255
            imageConvolue[i,j] = np.sum(image[i - c : i + c + 1, j - l : j + l + 1] * filtre)

    return imageConvolue

'''
def convolution2D(image, filtre):
    shape = np.shape(image) # (256, 256)
    imageConvolue = np.zeros(shape) # (256, 256) filled with 0 

    c = (filtre.shape[1]-1) // 2 
    l = (filtre.shape[0]-1) // 2 

    

    for imgJ in range((image.shape[1])): # COLONNE IMAGE
        for imgI in range((image.shape[0])): # LIGNE IMAGE
            #imageConvolue[i,j] = np.sum(image[i - c : i + c + 1, j - l : j + l + 1] * filtre)
            somme = 0
            nbPix = 0
            moyenne = 0
            for filtreJ in range(filtre.shape[1] - c, filtre.shape[1] + c): # COLONNE FILTRE
                for filtreI in range(filtre.shape[0] - l, filtre.shape[0] + l): # LIGNE FILTRE
                    nbPix += 1
                    if(dansImage(image, filtreJ, filtreI)):
                        somme = image[imgI, imgJ] * filtre[filtreI][filtreJ]
                    else:
                        somme = 0
                    
                moyenne = somme / nbPix

            imageConvolue[imgI][imgJ] = moyenne

    return imageConvolue
'''



def sumOfMatrix(matrix):
    totalSum = 0
    totalIndex = 0
    for j in range(matrix.shape[1]):
        for i in range(matrix.shape[0]):
            totalSum += matrix[i][j]
            totalIndex += 1
    return totalSum, totalIndex

#a = np.array([[1.2,2.5],[3.2,1.8],[1.1,4.3]])
#sum, total = sumOfMatrix(a)

print(sum)


def openImageInWindow(image):
    cv.imshow("", cellules)
    cv.waitKey()

def openImagesInWindow(image1, image2):
    plt.figure("title")
    
    plt.subplot(1,2,1)
    plt.imshow(image1, cmap='gray')

    plt.subplot(1,2,2)
    plt.imshow(image2, cmap='gray')

    plt.show()

#openImagesInWindow(cellules, convolution2D(cellules, np.ones(shape=(21, 5))))

openImagesInWindow(cellules, cv.blur(cellules, (21,21), borderType=cv.BORDER_CONSTANT))
