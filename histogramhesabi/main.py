import  cv2
import  numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from numpy import zeros, shape

foto=cv2.imread("indir.jpg",0)#histogram dizisindeki indeksler tam sayı olduğundan parametreye 0 vererek gri seviye görüntüyü elde ettim.Amaç pikselleri tam sayı olarak almaktır.

cv2.imshow("resim",foto)


histogram=zeros(256)

[satir,sutun]=shape(foto)

for row in range(0,satir):#burada satır kontrolu yapıyoruz
    for column in range(0,sutun):#burada belirli satırın sütunlarını geziyoruz

        i=foto[row,column]#ilgili piksel değerini alıyoruz

        histogram[i]=histogram[i]+1##sonra aldığımız piksel seviyesini 1 arttırıyoruz



print("histogram dizisi şu şekildedir:")

for i in range(0,256):
    print(histogram[i])






cv2.waitKey()




