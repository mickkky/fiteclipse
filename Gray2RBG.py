from PIL import Image
import os

count = 1
for filename in os.listdir(r"E:\\graysamples\\"):              #读取灰度样本文件

    filepath = "E:\\graysamples\\" + filename
    print(filepath)
    pic_gray = Image.open(filepath)

    pic_rgb = pic_gray.convert("RGB")                           #  灰度影像转RGB并保存
    print(pic_rgb.getpixel((0,0)))
    savepath = "E:\\RBG_samples\\" + str(count) + ".jpg"
    count = count + 1
    pic_rgb.save(savepath)