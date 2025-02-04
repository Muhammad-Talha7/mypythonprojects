import math
def menu():
    while True:
        ch=int(input("1. Convert binary to decimal\n2.Convert decimal to binary\n0. Exit\nEnter your choice: "))
        if ch>=0 and ch<=2:
            return ch
            break
        else:
            print("\t\t\tInvalid Choice")
def bi_to_dec():
    inp = input("\t\t\tEnter a binary number: ")
    bi = [int(digit) for digit in inp]
    dec=0
    y=1
    for x in range(len(bi)):
        dec+=bi[-(x+1)]*(2**x)
    return dec

def dec_to_bi():
    binary=[]
    inp=int(input("\t\t\tEnter a decimal number: "))
    while inp > 1 :
        binary.append(inp%2)
        inp=inp//2

    binary.append(inp)
    binary.reverse()
    return binary
while True:
    ch=menu()
    if ch==1:
        print("\t\t\t\t\t\t",bi_to_dec())
    elif ch==2:
        print("\t\t\t\t\t\t",dec_to_bi())
    elif ch==0:
        break
