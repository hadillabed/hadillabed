def hide(n):     #hide the last 4 digits of the credit card number
    string = str(n)
    hidden = "*"*(len(string)-4)
    res = hidden + string[-4:]
    return res
def disarium(nr): #disarium is when the sum of the digits of a nbr power their index equals the nbr
    dis=0
    str_nr=str(nr)
    for index,char in enumerate(str_nr): #enumerate usable for when you need the index and the elemnt of the index
        dis+=pow(int(char),index+1)
    if dis==nr:
        return True
    else:
        return False
#shifts a string to right per a nbr you enter
def ceasar_encrypt(str,nbr_shift):
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    res=[]
    str=str.lower() 
    for char in str:
        if char.isalpha():
            if char != "z":
                if char.islower():
                    res.append(alphabets[alphabets.index(char)+nbr_shift])
                else:
                    res.append(alphabets[alphabets.index(char)+nbr_shift].upper())
            else:
                res.append("a")
        else:
            res.append(char)
    return res
# string=input("enter : ")
# nbr=int(input("enter nbr of shift : "))
# print(ceasar_encrypt(string,nbr))
#we can use ASCII code using the function ord(char)
def inttostr(nbr): #conversion int to str
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
#spongcase: upper , lower case string
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
#encryption:
def encypt(string):
    dict_vow={"a":"0","e":"1","o":"2","i":"2","u":"3"}
    reversed=string[::-1]
    for char in reversed:
        if char in dict_vow:
            enc=reversed.replace(char,dict_vow.get(char))
    return enc+"aca"
