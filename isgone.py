def getstolen_items():
    stolen_items={}
    num_items=int(input("enter nbr of items:"))
    for i in range (num_items):
        item=input(f"enter the item {i+1} : ")
        qntity=1
        stolen_items[item]=qntity
    return stolen_items
def isgone(stolen_items,pet_name):
    if pet_name in stolen_items:
        return f"{pet_name.capitalize()} is gone"
    else:
        return f"{pet_name.capitalize()} is here"
stolen=getstolen_items()
pet=input("enter the pet : ")
print(isgone(stolen,pet))
