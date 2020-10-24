from PIL import Image


def cz(file, bl):
    img = Image.open(file)
    print(img.size)
    w, h = img.size
    blw = float(w) / bl[0]
    blh = float(h) / bl[1]

    if blw > 1 or blh > 1:
        blz = blw if blw > blh else blh
        img.thumbnail((w / blz, h / blz))
        print(img.size)
        img.save("thum.jpg", "JPEG")


cz("1.jpg", (116, 60))
