import random

from PIL import Image, ImageDraw,ImageFont

w = 60 * 4
h = 60
img = Image.new('RGB', (w, h), (255, 255, 255))
draw = ImageDraw.Draw(img);

for x in range(w):
    for y in range(h):
        draw.point((x, y),(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)))

str = "1234567890QWERTIPASFGHKLZVBNM"
font = ImageFont.truetype('arial.ttf', 36)
min = 10
max = 0
for i in range(4):
    min = i*60 + 10
    max = 60 * i + 60
    zf=random.choice(str)
    print(zf)
    # print(str(min)+""+str(max))
    draw.text((random.randint(min,max),random.randint(10,30)),zf,font=font,fill=(random.randint(32, 255), random.randint(32, 255), random.randint(32, 255)) )


img.save("11.jpg", "JPEG")
