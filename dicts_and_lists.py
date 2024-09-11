# def get_profit():
#     nbr_products=int(input("enter the nbr of the products : "))
#     products=[]
#     for i in range (nbr_products):
#         product={}
#         product_name=input("enter the prodct name : ").lower()
#         cost_price=float(input("enter the cost price: "))
#         sell_price=float(input("enter the sell price: "))
#         inventory=int(input("enter inventory: "))
#         profit=inventory*(sell_price - cost_price)
#         product['name']=product_name
#         product['cost price']=cost_price
#         product['sell price']=sell_price
#         product['inventory']=inventory
#         product['profit']=profit
#         products.append(product)
#     for product in products:
#         print(f"the profit of '{product['name']}' is: '{product['profit']}")
#     return products
# print(get_profit())
#gets high note of student : list and dict
def get_students():
    students={}    
    num_students=int(input("enter the num of students : "))
    for i in range(num_students):
        student=input("enter the name of the student :").lower()
        for j in range(2):
            list_of_notes=[]
            note=int(input("enter note : "))
            list_of_notes.append(note)
        students[student]=list_of_notes
    return students
def get_high_note(students):
    recherch=input("enter the name of the student you are looking for : ").lower()
    if recherch in students:
        list_n=students.get(recherch)
        high_note=max(list_n)
        return high_note
    else:
        return "no student with that name"
#returns the stolen item
def getstolen_items():
    stolen_items={}
    num_items=int(input("enter nbr of items:"))
    for i in range (num_items):
        item=input(f"enter the item {i+1} : ")
        qntity=1
        stolen_items[item]=qntity
    return stolen_items
def isgone(stolen_items,pet_name):
    if pet_name in stolen_items:
        return f"{pet_name.capitalize()} is gone"
    else:
        return f"{pet_name.capitalize()} is here"
# stolen=getstolen_items()
# pet=input("enter the pet : ")
# print(isgone(stolen,pet))
#sorted list:
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
#returns alternate list 
def alternate(n):
    str1="loves me"
    str2="loves me not"
    res=[]
    for i in range(n):
        if i%2==0: 
            res.append(str1)
        else: 
            res.append(str2)
    return res
#list generator and split()
def is_product_divisible_by_the_sum(numbers):
    if not numbers:
        return False
    else:
        total_sum=0
        product=1
        for i in range (len(numbers)):
            total_sum=int(numbers[i])+total_sum
            product=product*int(numbers[i])
        print(total_sum,"and",product)
        if total_sum==0:
            return False
        if product%total_sum==0: #if its divisible 
            return True
        else:
            return False
# numbers=input("enter numbers seperated by space : ").split()
# numbers=[int(num) for num in numbers] #i can use a generator instead of loop
# print(is_product_divisible_by_the_sum(numbers))
#get list for initialization , qualified verifies 
def get_list():
    list=[]
    nbr=int(input("enter the nbr of qst answered: "))
    for i in range (nbr):
        qst_time=int(input(f"enter the time for the qst {i+1}: "))
        list.append(qst_time)
    return list
def qualified (list,time):
    if len(list)==8:
        if time==120:
            if( (list[1]==5 and list[0]==5) and (list[2]==10 and list[3]==10) and (list[4]==15 and list[5]==15) and (list[6]==20 and list[7]==20)):
                return "qualified"
            else:
                return "disqualified"
        else: 
            return "disqualified"
    else:
        return "disqualified"
# print("___ enter the list of interview time___")
# lst=get_list()
# print("___ enter the interview time___")
# time=int(input("enter time of interview : "))
# print(qualified(lst,time))
#finds the highest nbr in a list
def find_highest(lst):
    if len(lst)==0: 
        return "no element in  the list"
    elif len(lst)==1:
        return lst[0]
    else:
        if lst[0]>lst[1]:
            lst.pop(1)
        else:
            lst.pop(0)
        return find_highest(lst)
#gets the users list:
def getusers_list():
    inp=input("enter a list of numbers seperated by spaces : ")
    list=[int(n.strip()) for n in inp.split()] #strip removes the spaces before or after the elements
    return list 
#consecutive sequence:
def consecutive_combo(lst1, lst2):
    lst=lst1.append(lst2)
    return lst
print("this",consecutive_combo([1,2],[3,4]))