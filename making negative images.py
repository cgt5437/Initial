from cImage import *

def negativePixel(originalPixel):
    
    newGreen = 255 - originalPixel.getGreen()
    newBlue = 255 - originalPixel.getBlue()
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel

def makeNegative(imageFile):
    myimagewindow = ImageWin("Image Processing" , 600, 200)
    oldimage = FileImage(imageFile)
    oldimage.draw(myimagewindow)

    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)
            newred= 255 - originalPixel.getRed()
            newgreen= 255 - originalPixel.getGreen()
            newblue= 255- originalPixel.getGreen()
            newPixel = (newred,newgreen,newblue)
        
            newim.setPixel(col,row,newPixel)

    
    
