import  cv2
import  numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

foto=cv2.imread("babon.jpg",0)

cv2.imshow("orijinal",foto)

satir,sutun=foto.shape


for i in range(0,satir):
    for j in range(0,sutun):
        foto[i][j]=np.max(foto)-foto[i][j]

cv2.imshow("inverted",foto)



cv2.waitKey()
