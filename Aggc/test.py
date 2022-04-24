import os
import cv2

path='D:\\BaiduNetdiskDownload\\Subset2_Train_annotation\\Subset2_Train_1'

files=os.listdir(path)

for file in files:
    imagepath=os.path.join(path,file)
    img = cv2.imread(imagepath)
    print(img)


