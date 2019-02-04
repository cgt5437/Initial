#This method takes the value from the first list and checks to see if it exists
#in the second list.  If all the values that exists in the first list exist in the
#second list as well, method return True.  If the lists do not contain all the
#same variables then it will return False.

#code was written by Christian Thomas and Zac Helmkampf

def areRearrangements(list1,list2):
    ListComparison = 0

    for i in list1:
        if i in list2:
            ListComparison = ListComparison + 0

        else:
            ListComparison = ListComparison + 1

    if ListComparison == 0:
        return True
    else:
        return False
    
