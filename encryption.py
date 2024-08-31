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
string=input("enter : ")
nbr=int(input("enter nbr of shift : "))
print(ceasar_encrypt(string,nbr))
#we can use ASCII code using the function ord(char)