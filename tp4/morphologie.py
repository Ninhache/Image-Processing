import OpenCVUtils as ou
import cv2 as cv


img = cv.imread("../images/smiley_nb.png")

SE_CROSS = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
SE_RECT = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
SE_ELLIPSE = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))


def openSimpleMorph(img, function):
    imgErode0 = function(img, SE_CROSS, iterations=0)
    imgErode1 = function(img, SE_CROSS, iterations=1)
    imgErode2 = function(img, SE_CROSS, iterations=2)
    imgErode3 = function(img, SE_CROSS, iterations=3)
    imgErode4 = function(img, SE_RECT, iterations=0)
    imgErode5 = function(img, SE_RECT, iterations=1)
    imgErode6 = function(img, SE_RECT, iterations=2)
    imgErode7 = function(img, SE_RECT, iterations=3)
    imgErode8 = function(img, SE_CROSS, iterations=0)
    imgErode9 = function(img, SE_CROSS, iterations=1)
    imgErode10 = function(img, SE_CROSS, iterations=2)
    imgErode11 = function(img, SE_CROSS, iterations=3)

    ou.showImages(imgErode0,imgErode1,imgErode2,imgErode3,imgErode4,imgErode5,imgErode6,imgErode7,imgErode8,imgErode9,imgErode10,imgErode11)

def openComplexMorph(img, function, associatedSE):
    imgErode0 = function(img, associatedSE, SE_CROSS, iterations=0)
    imgErode1 = function(img, associatedSE, SE_CROSS, iterations=1)
    imgErode2 = function(img, associatedSE, SE_CROSS, iterations=2)
    imgErode3 = function(img, associatedSE, SE_CROSS, iterations=3)
    imgErode4 = function(img, associatedSE, SE_RECT, iterations=0)
    imgErode5 = function(img, associatedSE, SE_RECT, iterations=1)
    imgErode6 = function(img, associatedSE, SE_RECT, iterations=2)
    imgErode7 = function(img, associatedSE, SE_RECT, iterations=3)
    imgErode8 = function(img, associatedSE, SE_CROSS, iterations=0)
    imgErode9 = function(img, associatedSE, SE_CROSS, iterations=1)
    imgErode10 = function(img, associatedSE, SE_CROSS, iterations=2)
    imgErode11 = function(img, associatedSE, SE_CROSS, iterations=3)

    ou.showImages(imgErode0,imgErode1,imgErode2,imgErode3,imgErode4,imgErode5,imgErode6,imgErode7,imgErode8,imgErode9,imgErode10,imgErode11)

#openSimpleMorph(img, cv.dilate)
openComplexMorph(img, cv.morphologyEx, cv.MORPH_GRADIENT)