import cv2 as cv
matrice = cv.imread("lena.png") # charge le fichier dans une matrice de pixels couleur

print(matrice.shape) # affiche les dimensions de la matrice
print(matrice[0,0]) # accède à la valeur du premier pixel