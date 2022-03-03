import cv2 as cv
import matplotlib.pyplot as plt

tmpImage = cv.imread("./images/canvas.png", 0)

def showImages(*images):
    plt.figure("title")
    
    nb_img = len(images)
    nb_col = 4 if nb_img > 4 else nb_img
    nb_row = nb_img // nb_col

    index = 0

    print("nb colonne : ", nb_col)
    print("nb ligne : ", nb_row)

    '''
    plt.figure("title")
    
    plt.subplot(1,1,1)
    plt.imshow(image1)    

    
    '''
    w = 10
    h = 10
    fig = plt.figure(figsize=(8, 8))
    columns = 4
    rows = 5
    for i in range(1, columns*rows +1):
        fig.add_subplot(rows, columns, i)
        plt.imshow(images[i])
        plt.show()
            

    plt.show()



showImages(tmpImage, tmpImage, tmpImage)
