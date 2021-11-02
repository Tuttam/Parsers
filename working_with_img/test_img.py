# import PIL
from PIL import Image, ImageDraw


img = Image.open("test3.png")

draw = ImageDraw.Draw(img)

# img2 = ImageDraw.ImageDraw.arc(xy, 5, 10, fill=None, width=5)
draw.arc(((1550, 850), (1610, 910)), 0, 110, fill=(85, 56, 122), width=10)
draw.arc(((1550, 50), (1610, -10)), 0, 110, fill=(0, 122, 0), width=10)


# img1 = img.resize((510, 412))

img.save("111.png")


print(img.size)
