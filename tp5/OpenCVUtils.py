import cv2 as cv
import matplotlib.pyplot as plt

def showImages(*images):
    plt.figure("Images...")
    
    nb_img = len(images)
    nb_col = min(4, nb_img)
    nb_row = ((nb_img-1) // nb_col)

    index = 1

    for row in range(nb_row +1):
        for col in range(nb_col):
                    
            plt.subplot(nb_row+1,nb_col,index)
            plt.imshow(images[index -1], 'gray')
            plt.axis("off")
            index = index + 1

            if(index > nb_img):
                break
        if(index > nb_img):
                break

    plt.show()