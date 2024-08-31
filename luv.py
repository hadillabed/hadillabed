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
n=int(input("enter a number : "))
print(alternate(n))     