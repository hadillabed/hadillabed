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
try:
    stri=input("enter :")
    print(arithmetic_operation(stri))
except ValueError as e:
    print(e)