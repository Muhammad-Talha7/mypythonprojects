str=input("Enter a encrypted message :")
n=int(input("Enter which ROT algo you want to apply: "))
str1=[]
for x in str:
    if x.isalpha():
        d=chr(ord(x)+n)
        if ord(d)>122:
            d=chr((ord(d)-123)+97)
    else:
        d=x    
    str1.append(d)
print("Decrypted Message: ","".join(str1))