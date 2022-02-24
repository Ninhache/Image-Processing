from multiprocessing.connection import wait
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

'''

cellules = cv.imread('cellules.png',0)

print(cellules.shape) # < dimension of the image

#height = img.shape[0]   # ici 176
#width = img.shape[1]    # ici 241
##channels = img.shape[2] # par defaut 3






'''

#print(histogramCumulFromImage(cellules))
#print(histogramFromImage(cellules))

def histogramFromImage(image):
    histograme = np.zeros(256, dtype=int)

    for w in image:
        for h in w:
            histograme[h] = histograme[h] + 1

    #print(histograme[65])
    return histograme

def histogramCumulFromImage(image):
    histograme = histogramFromImage(image)
    valeurActuel = 0
    idx = 0

    for item in histograme:
        valeurActuel = valeurActuel + histograme[idx]
        histograme[idx] = valeurActuel
        idx += 1
    
    return histograme


###############################
###############################
###############################

cellules=cv.imread("cellules.png",0)
#print(cellules.shape)

histCellules=histogramFromImage(cellules)
histCumCellules=histogramCumulFromImage(cellules)

plt.figure('Cellules')
NdG=np.linspace(0,255,256)
plt.subplot(1,4,1)
plt.imshow(cellules,cmap='gray')
plt.subplot(1,4,2)
plt.plot(NdG,histCellules,color='b',label='histogramme')
plt.xlabel('Niveau de gris')
plt.ylabel('Nombre de pixels')
plt.title('histogramme de Cellules')
#plt.plot(NdG,histCumCellules,color='r',label='histogramme cumulé')
'''
plt.plot(NdG,histCumCellules,color='b',label='histogramme2')
plt.xlabel('Niveau de gris')
plt.ylabel('Nombre de pixels')
plt.title('histogramme de Cellules')
'''

###############################
###############################
###############################

irm = cv.imread("irmCerveau.png",0)
histIRM=histogramCumulFromImage(irm)
#histCumIRM=histogrammeCumule(histIRM)

plt.figure('irmCerveau')
NdG=np.linspace(0,255,256)
plt.subplot(1,3,1)
plt.imshow(irm,cmap='gray')
plt.subplot(1,3,3)
plt.plot(NdG,histIRM,color='b',label='histogramFromImage')
#plt.gca().twinx().plot(NdG,histCumIRM,color='r',label='histogramme cumulé') # twinx : pour avoir 2 échelles différentes
plt.xlabel('Niveau de gris')
plt.ylabel('Nombre de pixels')
plt.legend()
plt.title('histogrammes de irmCerveau')

###############################
###############################
###############################


plt.show()