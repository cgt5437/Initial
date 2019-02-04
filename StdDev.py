

def findStdDev(alist):
    import math
    theMean= mean(alist)

    total=0
    for item in alist:
        difference=items-theMean
        diffsqrd=difference ** 2
        total=total+diffsqrd

        answer=math.sqrt(total/(len(alist)-1))
        return answer
