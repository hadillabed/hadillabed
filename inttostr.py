def inttostr(nbr):
    if isinstance(nbr,int):
        return str(nbr)
    else:
        raise ValueError("only integer input") #to handle an error
def strtoint(st):
    st=st.lower()
    if isinstance(st,str):
        return int(st)
    else:
        raise ValueError("only string input!!!")
nbr=int(input("enter an int: "))
print(inttostr(nbr))
stri=input("enter a string: ")
print(strtoint(stri))
