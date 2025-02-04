from pathlib import Path
def change_pass():
    che=check_pass()
    if che==True:
        f=open("password.txt","w")
        f.write(input("\t\t\tEnter your new password: "))
    elif che==False:
        print("Invalid Password")
def check_pass():
    f=open("password.txt","r")
    f=f.read()
    pas=input("\t\t\tEnter your password: ")
    if pas==f:
        return True
    else:
        return False
def create_file():
    f=open("password.txt","x")

def menu():
    while True:
        print("1. Enter Password \n2. Change Password \n0. Exit")
        i=int(input("Enter your choice: "))
        if i<=2 and i>=0:
            return i
            break
        else:
            print("Invalid choice")

#if file dont exsist run this code
file_path= Path("password.txt")
if not file_path.exists():
    create_file()
    f=open("password.txt","w")
    f.write(input("Set a password: "))
else:
    
    ch=menu()
    if ch==0:
       print() 
    elif ch==1:
        ch1=check_pass()
        print("\t\t\t",ch1)
    elif ch==2:
        change_pass()

