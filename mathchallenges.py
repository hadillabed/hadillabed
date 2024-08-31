import math
from math import pi
def radtodeg(float):
    return round(float * (180/pi) , 1) #to round a specific nbr of the decimal
                                        #part
ex=float(input("enter : "))
print(radtodeg(ex))
def cicur(rad,area):
    circm=2*pi*rad
    perim=4*math.sqrt(area)
    if circm>perim:
        return True
    else:
        return False
rad,area=int(input("enter radis : ")), int(input("enter area : "))
print(cicur(rad,area))
def end_corona(recovers,newcases ,currcases):
    if recovers>newcases:
        r=recovers-newcases
    return math.ceil(currcases/r)
recovers,newcases,currcases=int(input("enter recovers: ")),int(input("enter newcases : ")), int(input("enter currcases: "))
print(end_corona(recovers,newcases,currcases))
