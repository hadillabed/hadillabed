def calculator():
    nb1=int(input("enter your nbr1: "))
    nb2=int(input("enter your nbr2: "))
    oper=input("enter your operator: ")
    if oper=="*":
        return nb1*nb2
    elif oper=="+":
        return nb1+nb2
    elif oper=="-":
        return nb1-nb2
    elif oper=="/":
        if nb2==0:
            raise ArithmeticError("cant divide by 0")
        else:
            return nb1/nb2
    else:
        print("invalid operator")

print(calculator())