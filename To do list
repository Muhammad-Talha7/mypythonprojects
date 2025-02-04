def choice():
    while True:
        x = int(input("\n Enter your choice: "))
        if 0 <= x <= 3:
            return x
        else:
            print(" Invalid Choice\n")
def choice1():
    while True:
        print("\n \t\t\t1. Add another task")
        print(" \t\t\t0. Go back")
        x = int(input("\n \t\t\tEnter your choice: "))
        if 0 <= x <= 1:
            return x
        else:
            print(" Invalid Choice\n")
def enter_item():
    list=input("\n \t\t\tEnter a task: ")
    return list
    
toDoList = []
while True:
    print("\n  1. Enter item in to do list")
    print("  2. Show to do list")
    print("  3. Remove Item from the list")
    print("  0. Exit")
    ch=choice()
    if ch==0:
        break
    elif ch==1:
        ch1=1
        while ch1==1:
            x=enter_item()
            toDoList.append(x)
            ch1=choice1()
    elif ch==2:
        y=1
        for t in toDoList:
            print(" \t\t\t",y,". ",t)
            y=y+1
    elif ch==3:
        y=1
        for t in toDoList:
            print(" \t\t\t",y,". ",t)
            y=y+1
        ch2=int(input("\n\t\t\tEnter a item number to delete: "))
        if 1 <= ch2 <= len(toDoList):   
            toDoList.pop(ch2 - 1)
            print(f"\n \t\t\tItem number {ch2} has been deleted.")
        else:
            print("\n Invalid item number.")
