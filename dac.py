import math
def v_dac(dec):
    if dec==0:
        return 0
    elif dec==1023:
        return 5
    else:
        return round(dec*5/1023,2)
tri=int(input("enter a decimal number : "))
print(v_dac(tri))