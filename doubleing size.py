from cImage import *
def doublingSize(Fileimage):
    oldimage = FileImage(Fileimage)
    oldw= oldimage.getWidth()
    oldh= oldimage.getHeight()

    newim = EmptyImage(oldw*2, oldh*2)

    for row in range(oldh):
        for col in range(oldw):
            oldPixel = oldimage.getPixel(col, row)

            newim.setPixel(2*col,2*row, oldPixel)
            newim.setPixel(2*col+1,2*row, oldPixel)
            newim.setPixel(2*col,2*row+1,oldPixel)
            newim.setPixel(2*col+1,2*row+1,oldPixel)
    myWin = ImageWin('big image', 1200,400)
    newim.draw(myWin)
