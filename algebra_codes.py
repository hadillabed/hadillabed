# def mimiics(nbr1,nbr2):
#     return round( nbr1/pow(2,nbr2))
# nbr1,nbr2=int(input("enter nbr 1: ")), int(input("enter nbr2: "))
# print (mimiics(nbr1,nbr2))
# def find_highest(lst):
#     if len(lst)==0: 
#         return "no element in  the list"
#     elif len(lst)==1:
#         return lst[0]
#     else:
#         if lst[0]>lst[1]:
#             lst.pop(1)
#         else:
#             lst.pop(0)
#         return find_highest(lst)
def getusers_list():
    inp=input("enter a list of numbers seperated by spaces : ")
    list=[int(n.strip()) for n in inp.split()] #strip removes the speaces before or after the elements
    return list 
# users_list=getusers_list()
# print("the highest numbers in your list is : ",find_highest(users_list))   
# def number_length(num):
#     length=0
#     for i in str(num):
#         length += 1
#     return length
# nbr=int(input("enter a numbr: "))
# print(number_length(nbr))
# def fizzbuzz(nnr):
#     if (nnr%3==0 and nnr%5==0):
#         return "FizzBuzz"
#     elif nnr%3==0:
#         return "Fizz"
#     elif nnr%5==0:
#         return "Buzz"
#     else:
#         return str(nnr)
# nbr=int(input("enter a numbr: "))
# print(fizzbuzz(nbr))
import math
def length_of_segment(coor1,coor2):
    # coor=[coor1,coor2]
    if len(coor1)!=2 or len(coor2)!=2:
        return "enter only x and y coordinates"
    else:
        res=round(math.sqrt(pow(coor2[0]-coor1[0],2)+pow(coor2[1]-coor1[1],2))) #(coor2[1]-coor1[1] ** 2 is same as power
        return res
ls1=getusers_list()
ls2=getusers_list()
print(length_of_segment(ls1,ls2))