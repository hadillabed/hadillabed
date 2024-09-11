#calculates the length of a seg using two coordinates
import math
def length_of_segment(coor1,coor2):
    # coor=[coor1,coor2]
    if len(coor1)!=2 or len(coor2)!=2:
        return "enter only x and y coordinates"
    else:
        res=round(math.sqrt(pow(coor2[0]-coor1[0],2)+pow(coor2[1]-coor1[1],2))) #(coor2[1]-coor1[1] ** 2 is same as power
        return res
#calculate the difference between two square areas using a circle radius inside
def diff_square_areas(): 
    rad=int(input("enter the radius : "))
    sq1_area=(2*rad)**2
    sq2_area=(rad*math.sqrt(2))**2
    return round(sq1_area - sq2_area)
print(diff_square_areas())
#snake game: returns how many times the snake can eat before it runs out of space
def snake(n):
    area_game=n*n
    snake_len=1
    times=0
    while snake_len*2<area_game:
        snake_len*=2
        times+=1
    return times