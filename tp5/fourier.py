import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import OpenCVUtils as ou

image = cv.imread("../images/canvas.png", 0)
nb = 5

def toFreqDomain(image):
	return np.fft.fft2(image)

def module(freq):
	return np.abs(freq)

def logarithm(freq):
	return np.log(freq)

def shift(freq):
	return np.fft.fftshift(freq, axes=(1,0))


def setMask(image, nb):
	width = image.shape[0]
	height = image.shape[1]
	image[ (width // 2) - nb : (width // 2) + nb , (height // 2) - nb : (height // 2) + nb ] = 0

tf = toFreqDomain(image)
shiftTf = shift(tf)
moduletf = module(shiftTf)
logTf = logarithm(moduletf)




#plt.imshow (logarithm(module(toFreqDomain(image))))
setMask(logTf, 21)

plt.imshow(logTf)
plt.show()