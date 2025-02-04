def pw(n,p):
    if p==1:
        return n
    else:
        return n*pw(n,p-1)
    
print(pw(2,3))