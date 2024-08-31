def luke_family(string):
    string= string.lower()
    if string=="darth vader":
        return ("luke i am your father")
    elif string =="leia":
        return("luke i am your sister")
    elif string == "han":
        return("luke i am your brother in law")
    elif string=="r2d2":
        return("luke i am your droid")
    else:
        return ("idk")
str=input("enter your name: ")
print(luke_family(str))