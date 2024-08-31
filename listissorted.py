def listissorted( list ):
    asc , desc = True,True
    if (len(list)<1):
        return True
    for i in range (len(list)-1):
        if (list[i]<list[i+1]):
            desc= False
    for i in range (len(list)-1):
        if (list[i]>list[i+1]):
            asc=False
    return asc or desc
list=[1,2,3,4]
print(type(list))
print(listissorted(list))
      