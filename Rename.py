from PIL import Image
import os
count = 1
for filename in os.listdir(r"E:\\triandata\\"):              #读取灰度样本文件

    filepath = "E:\\triandata\\" + filename
    print(filepath)
    pic = Image.open(filepath)
    temp = pic
    #pic_rgb = pic.convert("RGB")                           #  灰度影像转RGB并保存
   #  print(pic_rgb.getpixel((0,0)))
    if count < 10:
        savepath = "E:\\Example\\" +"00000" + str(count) + ".jpg"
        count = count + 1
        temp.save(savepath)

    elif count >=10 and count <100:
        savepath = "E:\\Example\\" + "0000" + str(count) + ".jpg"
        count = count + 1
        temp.save(savepath)

    elif count >=100 and count <1000:
        savepath = "E:\\Example\\" + "000" + str(count) + ".jpg"
        count = count + 1
        temp.save(savepath)

    elif count >=1000 and count <10000:
        savepath = "E:\\Example\\" + "00" + str(count) + ".jpg"
        count = count + 1
        temp.save(savepath)

   # savepath = "E:\\Example\\" + str(count) + ".jpg"
   #  count = count + 1
   #  temp.save(savepath)