from PIL import Image,ImageDraw,ImageFile
import os
def  createTu(img):
   draw=ImageDraw.Draw(img)
   color='#ff0000'
   w,h=img.size
   draw.text((w-10,0),"99")
   img.save('result.jpg','jpeg',fill=color)


createTu(Image.open(os.getcwd()+"\\1.jpg"));
