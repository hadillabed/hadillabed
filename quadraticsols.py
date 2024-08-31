class null_a(Exception):
    def __init__(self, a):
        if a==0:
            super().__init__("Enter a non null a")
def quad_sols(a,b,c):
    if a==0:
        raise null_a(a)
    else:
        delta=pow(a,2)-4*a*c
        if delta<0:
            return "no sol"
        elif delta ==0:
            return "one sol"
        else:
            return "2 sol"
try:
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=int(input("enter c : "))
    print(quad_sols(a,b,c))
except null_a as e:
    print(e)
    