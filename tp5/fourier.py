import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import OpenCVUtils as ou

def freq_pass(fft, window, factor):
    prop_window=np.multiply(window, fft.shape).astype(int)

    mask=np.ones(fft.shape)*factor[1]

    cx=int(fft.shape[0]/2) # width / 2
    cy=int(fft.shape[1]/2) # height / 2
    sx=int(prop_window[0]/2) # size x
    sy=int(prop_window[1]/2) # size y
    
    mask[cx-sx:cx+sx,cy-sy:cy+sy]=factor[0]

    return fft * mask

def low_pass(fft, window):
    return freq_pass(fft, window, (1, 0))

def high_pass(fft, window):
    return freq_pass(fft, window, (0, 1))

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

def subplot(x,y):
	xSize = 4
	ySize = 2
	plt.subplot(ySize, xSize, x + ((y-1)*xSize))

def plotImage(x,y, image, title):
	subplot(x,y)
	plt.axis("off")
	plt.title(title)
	plt.imshow(image, cmap='gray')

def plotFft(x,y, fft, title):
	subplot(x,y)
	plt.title(title)
	plt.imshow(np.log(np.abs(fft)), cmap='nipy_spectral')

#tf = toFreqDomain(image)
#shiftTf = shift(tf)
#moduletf = module(shiftTf)
#logTf = logarithm(moduletf)

#newImage = setMask(logTf.copy(), 7)

image1 = cv.imread("../images/lena.png", 0)
image2 = cv.imread("../images/canvas.png", 0)
#imageFlou = ajoutBruit(image)

def plotColumn(index, image, func):
	fft = np.fft.fftshift(np.fft.fft2(image))
	fft_shift = fft
	fft_shift=func(fft, (0.05, 0.05))
	source_shift = np.abs(np.fft.ifft2(fft_shift))


	plotImage(1,index, image, "1) Original")
	plotFft(2,index, fft, "2) Fft")
	plotFft(3,index, fft_shift, "3) IFft")
	plotImage(4,index, source_shift, "4) Image")

plotColumn(1, image1, low_pass)
plotColumn(2, image2, low_pass)

plt.show()