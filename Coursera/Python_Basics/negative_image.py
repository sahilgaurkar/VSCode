from PIL import Image

img = Image.open("luther.jpg")
print(img)

win = img.width , img.height

for row in range(img.height):
    for col in range(img.width):
        p = img.getpixel(col, row)

        newred = 255 - img.
        newgreen = 255 - p.getgreen()
        newblue = 255 - p.getblue()

        newpixel = (newred, newgreen, newblue)

        img.setpixel(col, row, newpixel)

img.draw(win)
win.exitonclick()



"""
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()
"""