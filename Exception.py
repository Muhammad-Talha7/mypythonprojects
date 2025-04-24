# Using exceptions

try:
    i=int(input("Enter an int :"))
except:
    print("Not an integer")
else:
    print(f"Integer = {i}")


# using pass
while True:
    try:
        i=int(input("Enter an int :"))
    except:
        pass    #continue
    else:
        print(f"Integer = {i}")
        break


# inputing an integer
while True:
    try:
        i=int(input("Enter an int :"))
        break
    except:
        print("Not an integer")

print(f"Integer = {i}")
