from cv2 import Sobel
import numpy as np

# GRADIENT'S MASK
robert3d    = np.array([[0,0,0], [-1,0,1], [0,0,0]])
prewitt     = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
sobel       = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])

# LAPLACIEN'S MASK
laplacien1  = np.array([[0,1,0], [1,-4,1], [0,1,0]])
laplacien2  = np.array([[1,1,1], [1, 8,1], [1,1,1]])