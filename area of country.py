# def area_of_country(name,area):
#     proportion = round((area / 148940000)*100 , 2)
#     return f"{name} is {proportion}% of the worldmass" #or proportion:.2f
# name=input("enter the name of the country : ")
# area=float(input("enter the area of the country : "))
# print(area_of_country(name,area))
def divisible_by_b(a,b):
    c=max(a,b)+1
    # if c%b==0:
    #     return f"the nbr greater than {a} and {b} is {c}"
    # else:
    #     while c>0 :
    #         c+=1
    #         if c%b==0:
    #             return f"the nbr greater than {a} and {b} is {c}"
    #             break
    while (c%b!=0):
        c+=1
    return f"the nbr greater than {a} and {b} and divisible by {b} is {c}"
a=int(input("enter a : "))
b=int(input("enter b : "))
print(divisible_by_b(a,b))