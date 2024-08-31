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
print("___ enter the list of interview time___")
lst=get_list()
print("___ enter the interview time___")
time=int(input("enter time of interview : "))
print(qualified(lst,time))