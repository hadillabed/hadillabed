import time #this bib contains everything concerning time
import math #importing bibs is important
#print("hi") string
name = "hi"
print (name + " hello")
print (type(name))
first_name="salam"
seocnd_name="alikoum"
hi = first_name+" "+seocnd_name
print (hi)
#int
age=18
print (type(age))
age += 1  #age = age + 1
print("your age is"+str(age)) #or just ,age
#float
height=1.91
print("your height is ",height, "cm") #same as int
#boolean
human=False
print (type(human))
#multiple assignment
namef, ge, heigh = "hadil labed", 19, 1.68
print(namef)
#if the variables are equal 
h = r = 40
print (h)
#string methods
print(len(namef)) # length function
print (namef.find("i")) #index of the letter 
print(namef.capitalize()) #capitalize only the first letter of the sentence
print(namef.upper()) #capitalize all the letters in the word
print(namef.lower()) #makes the letters small
print(namef.isdigit()) #returns boolean when the string is a digit
print (namef.isalpha()) #if the name was only alphabets and numbers with no space in between
print (namef.count("a")) #COUNTS how many caracters are in the word
print(namef.replace("a","o")) #replaces car with car
print(namef*3)#prints string number we want
#type casting = converting the type of variables 
x=1
y=2.0
z="3"
z=int(z)
print (str(x)*3)
print (int(y)) #we have all the types float , str , int ,...
print(z+1)
print ("this is"+str(x))
#inputs : the input is always a string
#t= input("what is your name ") #we stock as a var to reuse it later
#print ("my name is "+t)
#age= input ("what is your age? ") #or age= int(input("age"))
#age= int(age)+1
#print ("my age is "+str(age))
#hei=float(input("how tall are you? "))
#print("i am "+str(hei)+ " cm")
#import math
pi = 3.14
print (round(pi)) #ta9rib 
print(math.ceil(pi)) #t9arbo to the upper number
print(abs(pi))# the absolute value
print(pow(pi,2))#the power
print(math.sqrt(4)) #jidr tarbi3i
#print(max(age,int(hei),int(pi))) #max between numbers
#print(min(age,int(hei),int(pi))) #min 
#slicing : substracting a string from another string (indexed [start:stop:step], command slice(start,stop,step))
first= namef[:5] # we can write namef[0:...]
family= namef[6:] # [6:10]
funky= namef[::2] # [0:10:2]
reversed=namef [::-1]
print(first," ",family," ",funky," ",reversed)
web="https://google.com"
#website = input("write a url to a webiste like this https://google.com :")
#slice = slice(8,-4) #we go from left to right "beginning""kchghl bdina nhsbo mn 1" and the opposite for "stop"
#print("the website name is: " +website[slice])
#if conditional:
#f = input("your name:")
#if f[1]=="h":       #dont forget the : and the tab and ==
   # print("yes")
#elif f[2]=="a":
   # print("meow")
#else:
   # print("no")
#logical operators(and,or,not) to check two or more conditional statements
#temp=int(input("what is temperature outside?"))
#if not(temp<=30 and temp>0):  #not just works the opposite
    #print("go outside")
#elif temp<0 or temp>30:
   # print("stay at home")
#while loop
#n=input("enter yout name:")
#while len(n)== 0:
    #n=input("enter yout name:")
#print("hello"+" "+n)
#for loops : for i in range (start,stop,step):
#s=0
#for i in range (1,10+1,2):
    #s=s+i
#print (s)
#can be used for strings also: but just delete range
#for i in (n):
    #print(i)
#for seconds in range (1,5,1):
    #print(seconds)
    #time.sleep(1) #this means it will sleep for 2 sec after every iteration
#print ("you passed 10 secs") 
#nested loops : loop inside a loop 
# rows= int(input("how many rows:"))
# columns=int(input("how many columns :"))
#symbol=input("enter the symbol you want:")
##for i in range (rows):
     #for j in range(columns):
         #print(symbol, end="") #end="" will prevent to sauter la ligne
    #print() #print new line
#loop control statements
#break : terminate the loop entirely
#continue: it skips to the next iteration of the loop
#pass: it does nothing , it acts as a placeholder
#while True: #True is capitalized
   # nam= input("nter your name:")
    #if nam !="":
        #break
#phone = input ("enter your phone number with dashes")
#for i in phone:
   # if i=="-":
      #   continue
   # print (i, end="")
for i in range(1,21):
    if i == "13":
        pass
    else:
        print (i)
#list : to declare many items in one variable
food = ["jari","roz","dwida","barboucha"] #[]: are used for lists
food[0]= "chorbafrik"
food.append("pizza") # add an element to the list
food.remove(food[1]) #remove an element
food.pop() #removes the last element
food.insert(2,"mahjouba") #adds the element at the given index
food.sort() # sort the list alphabetically
food.clear() #removes all the list
for i in food:
    print (i, end=" ")   #end = " " after every element it will let a space 
#2D lists: a list of lists
drinks=["soda","milk","orange jus"]
fast=["hamburger","pizza"]
food =[drinks,fast]
print (food) #print(food[0][1]) : to print only one list or an element from a list
#tuple: a collection which is ordered and unchangeable used to group together related data
student=["bro",21,"male"]
print (student.count("bro"))
print(student.index(21))# it shows the index of an element li 7na ndakhloh
for x in student:
    print(x, end=" ")
if "bro" in student:
    print("bro is here")
#set= collection which is not ordered and unidexed , no duplicate values
utn = {"hadil","labed","only"}
nn={"hi","hello","hadil"}
#utn.update(nn) : it adds the element of nn in utn so when you print utn u find the elements of utn and nn
#utn.add("soon") : adds an element to the set utn 
#utn.remove("labed") : removes 
#utn.clear() : clear all the set
#intro = utn.union(nn) : the union of two sets
#for x in intro:
     #print(x, end=" ")
print(utn.difference(nn)) # the elements that are in utn and not in nn
print (utn.intersection(nn)) # the elements in common
#dictionary: unordered , changeable collection of unique key: value pairs fast bcz they use hashing , allow us to access a value quickly
capitals={'palestine':'al quds',
        'algeria':'algiers',
        'israel':'doesnt exist',
        'saudiarabia':'riyadh'}
#print(capitals["palestine"])
capitals.update({'germany':'berlin'}) #adds
capitals.update({'israel':'kkhra'})#modify
capitals.pop('germany') #removes
capitals.clear() #remove all items
#print(capitals.get('morroco')) #returns none when the key doesnt exist
print(capitals.values()) #return the values only
print(capitals.keys())# only keys
print(capitals.items())#entire dictionary
for key,value in capitals.items(): #returns all the keys andvalue without "dict_keys"...
    print(key, value)
#index operator[]: acess to sequence elements (str,list,tuples)
nom="hadil"
#if (nom[0].islower()):
    #nom = nom.capitalize()
f_nom= nom[:2].capitalize()
la_nom= nom[2:]
last_carac=nom[-1] #last element
print(f_nom,end=" ")
print(la_nom)
print(last_carac)
#function: block of code exucte when it s called
def hello(): #always wtih ()
    print("hello")

hello() #calling it 
#function with parameter
def gg(name,fname,age):
    print("gg "+name+" "+fname,age) #, age or +str(age)
gg("k","kiki",21)
#return statement : send values\objects back to the caller
def multiply (n1,n2):
    return n1*n2
print(multiply(6,8)) #we have to print it bcz return doesnt print, we can store it in a var
#keywords arguments : they are procede by identifier when we pass them to a function , the order isnt important unlike positional arguments used above
def call(num,name):
    print ("calling..."+name+" "+num)
call(num="+213778946547",name="hadil")
#nested functions calls : we use the return of a function as an argument for another function
#print(round(abs(float(input("enter a whole positive number:")))))
#scope=variable is availabe in the region where it is declared
name="hadil" #global vari /scope
def display_name(): #local variable
    name="code"        #functions usually use : local - enclosing - global - built in (LEGB rule)
    print(name)
display_name()
print(name)
# *args = * hiya li turni el arguments to a tuple
def add (*args): #like this we can use a function with 2 arguments to more args
    sum=0  #we can name it whataver we want
    for i in args:   #with tuples its ordered 
        sum += i #sum = sum + i
    return sum
print(add(1,2,3,4))
# **kwargs = pack all arg into a dictionary
def hello(**kwargs): #keywords arguments 
    #print("hello "+ kwargs['fir']+ " "+ kwargs['las'])
    print("hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello(title="dr",fir="hadil",mid="bouderbala",las="labed")
#str.format(): optional method tthat gives the user more control in output
animal = "kabyle"
planet="moon"
print ("the {} jumped over the {}".format(animal,planet)) #positional arguments
print ("the {1} jumped over the {0}".format(animal,planet))
#print ("the {} jumped over the {}".#format(animal="meow",planet="mercury"))