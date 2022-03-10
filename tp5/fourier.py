import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import OpenCVUtils as ou

def low_pass(fft, window):
    return freq_pass(fft, window, (1, 0))

def high_pass(fft, window):
    return freq_pass(fft, window, (0, 1))

def freq_pass(fft, window, factor):
    prop_window=np.multiply(window, fft.shape).astype(int)

    mask=np.ones(fft.shape)*factor[1]

    cx=int(fft.shape[0]/2) # width / 2
    cy=int(fft.shape[1]/2) # height / 2
    sx=int(prop_window[0]/2) # size x
    sy=int(prop_window[1]/2) # size y
    
    mask[cx-sx:cx+sx,cy-sy:cy+sy]=factor[0]

    return fft * mask


def ajoutBruit(image):
	row,col= image.shape
	mean = 0
	var = 100
	sigma = var**0.5
	gauss = np.random.normal(mean,sigma,(row,col))
	gauss = gauss.reshape(row,col)
	imageBruitee = image + gauss
	return imageBruitee


def setMask(image, nb):
	
	width = image.shape[0]
	height = image.shape[1]
	image[(width // 2) - nb : (width // 2) + nb , (height // 2) - nb : (height // 2) + nb ] = 0
	return image



#tf = toFreqDomain(image)
#shiftTf = shift(tf)
#moduletf = module(shiftTf)
#logTf = logarithm(moduletf)

#newImage = setMask(logTf.copy(), 7)

image = cv.imread("../images/canvas.png", 0)
#imageFlou = ajoutBruit(image)
nb = 5

fft = np.fft.fftshift(np.fft.fft2(image))
fft_shift = fft
fft_shift=high_pass(fft, (0.05, 0.05))
source_shift = np.abs(np.fft.ifft2(fft_shift))




ou.showImages(image, source_shift)
plt.show()