def hide(n):     #hide the last 4 digits of the credit card number
    string = str(n)
    hidden = "*"*(len(string)-4)
    res = hidden + string[-4:]
    return res
n=int(input("enter : "))
print(hide(n))