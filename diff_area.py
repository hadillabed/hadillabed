import math
def diff_square_areas():
    rad=int(input("enter the radius : "))
    sq1_area=(2*rad)**2
    sq2_area=(rad*math.sqrt(2))**2
    return round(sq1_area - sq2_area)
print(diff_square_areas())