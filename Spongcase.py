def spongcase (str):
    res=[]
    i=0
    for char in str:
        if char.isalpha(): #if char is alphabet
            if i%2==0: #even
                res.append(char.lower())
            else:
                res.append(char.upper())
            i+=1
        else:
            res.append(char)
    return res
string=input("enter : ")
print(spongcase(string))