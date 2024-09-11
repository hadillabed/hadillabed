def signup():
    print("signup")
    user_name=input("enter the username:")
    password=input("enter the password:")
    return user_name,password
def login(user_name,password):
    print("login")
    user_input=input("enter your account username: ")
    if user_input==user_name:
        password_input=input("enter your account password: ")
        if password_input==password:
            print("logged in successfully")
        else:
            print("wrong password")
    else:
        print("wrong username")
    print("login again")
username,password=signup()
login(username,password)