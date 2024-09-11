#calculates the proportion of a country of the world mass function
def area_of_country(name,area):
    proportion = round((area / 148940000)*100 , 2)
    return f"{name} is {proportion}% of the worldmass" #or proportion:.2f
# name=input("enter the name of the country : ")
# area=float(input("enter the area of the country : "))
# print(area_of_country(name,area))
#returns the nbr greater than a and b , divisible by b
def divisible_by_b(a,b):
    c=max(a,b)+1
    if c%b==0:
        return f"the nbr greater than {a} and {b} is {c}"
    else:
        while c>0 :
            c+=1
            if c%b==0:
                return f"the nbr greater than {a} and {b} is {c}"
                break
    while (c%b!=0):
        c+=1
    return f"the nbr greater than {a} and {b} and divisible by {b} is {c}"
# a=int(input("enter a : "))
# b=int(input("enter b : "))
# print(divisible_by_b(a,b))
# radian to gradient
import math
from math import pi
def radtodeg(float):
    return round(float * (180/pi) , 1) #to round a specific nbr of the decimal
                                        #part
def cicur(rad,area):
    circm=2*pi*rad
    perim=4*math.sqrt(area)
    if circm>perim:
        return True
    else:
        return False
# rad,area=int(input("enter radis : ")), int(input("enter area : "))
# print(cicur(rad,area))
def end_corona(recovers,newcases ,currcases):
    if recovers>newcases:
        r=recovers-newcases
    return math.ceil(currcases/r)
#recovers,newcases,currcases=int(input("enter recovers: ")),int(input("enter newcases : ")), int(input("enter currcases: "))
# print(end_corona(recovers,newcases,currcases))
#morse code : converts string to morse code using dictionary 
def string_to_morse(stri):
    char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    stri=stri.upper()
    for char in stri:
        stri=stri.replace(char,char_to_dots.get(char)+" ")
    return stri
# print(string_to_morse("hadil"))
#do a arithmetic operation out of a string
def arithmetic_operation(stri):
    splits=stri.split() #splits the str by spaces
    nb1=int(splits[0])
    oper=splits[1]
    nb2=int(splits[2])
    if oper=="+":
        return nb1 + nb2
    elif oper=="-":
        return nb1 - nb2
    elif oper=="*":
        return nb1*nb2
    elif oper=="//":
        if nb2==0:
            return -1
        else:
            return round(nb1/nb2,2)
    else:
        raise ValueError("invalid operator")
# try:
#     stri=input("enter :")
#     print(arithmetic_operation(stri))
# except ValueError as e:
#     print(e)
#dac : converts decimal to dac
def v_dac(dec):
    if dec==0:
        return 0
    elif dec==1023:
        return 5
    else:
        return round(dec*5/1023,2)
#returns nbr of solutions of a quadratic
class null_a(Exception):
    def __init__(self, a):
        if a==0:
            super().__init__("Enter a non null a")
def quad_sols(a,b,c):
    if a==0:
        raise null_a(a)
    else:
        delta=pow(a,2)-4*a*c
        if delta<0:
            return "no sol"
        elif delta ==0:
            return "one sol"
        else:
            return "2 sol"
#length of an int using str methods
def number_length(num):
    length=0
    for i in str(num):
        length += 1
    return length
#rate problem: 20mph speed in 18min
def ave_spd(time_up_mins,speed_up,speed_down):
    time_up_hours=time_up_mins/60
    distance_up=speed_up*time_up_hours
    time_down_hours=distance_up/speed_down
    total_time_hours=time_down_hours+time_up_hours
    total_distance=distance_up*2
    speed_avr=total_distance/total_time_hours
    return int(speed_avr)
#pentagonal:
def pentagonal(n):
    dots = (n * (3 * n)) // 2
    return dots
print(pentagonal(3))