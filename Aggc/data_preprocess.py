import os
import time
import cv2
import imageio

from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

# change it to your path
# also can modify to translate three subset same time
path='D:\\BaiduNetdiskDownload\\Subset2_Train_image'
mask_path='D:\\BaiduNetdiskDownload\\Subset2_Train_annotation'
dis="D:\\BaiduNetdiskDownload\\Subset2_Train"
mask_dis="D:\\BaiduNetdiskDownload\\mask"


crop_size=(640,640)

# place to store imgs
files=os.listdir(path)

def resize():
    for file in files:
        imagepath = os.path.join(path, file)
        img = cv2.imread(imagepath)
        print(crop_size)
        img_new = cv2.resize(img, crop_size, interpolation=cv2.INTER_CUBIC)  # 立方插值
        imageio.imsave(imagepath, img_new)




try:
    os.makedirs(dis)
except Exception as e:
    print(e)

def turn_jpg(imagepath,file):
    image = Image.open(imagepath)
    distImagePath = os.path.join(dis, file[:-4] + 'png')
    image.save(distImagePath)
    print(distImagePath)

# turn all the imgs into jpg format
def turn_all():
    for file in files:
        imagepath = os.path.join(path, file)
        turn_jpg(imagepath,file)


mask_files=os.listdir(mask_path)

def turn_mask(type):
    for file in files:
        img_name = file[:-5]
        for mask_file in mask_files:
            if mask_file == img_name:
                try:
                    imagepath = os.path.join(mask_path, mask_file, type+".tif")
                    print(imagepath)
                    if not os.path.exists(imagepath):
                        img = Image.new("RGB", (640, 640))
                        img.save(os.path.join(mask_dis, type, img_name + '.png'))
                        continue
                    img = cv2.imread(imagepath)
                    print(img)
                    print(crop_size)
                    img_new = cv2.resize(img, crop_size, interpolation=cv2.INTER_CUBIC)  # 立方插值
                    imageio.imsave(imagepath, img_new)

                    image = Image.open(imagepath)
                    distImagePath = os.path.join(mask_dis,type, img_name + '.png')
                    print(distImagePath)
                    image.save(distImagePath)
                except Exception as e:
                    img = Image.new("RGB",(640,640))
                    img.save(os.path.join(mask_dis,type, img_name + '.png'))

if __name__ == '__main__':
    # resize and turn to png
    resize()
    turn_all()
    turn_mask('Normal_Mask')














# extract mask

