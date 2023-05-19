def Fibnum(n) :
    if n < 2 :
        return n 
    return Fibnum (n-1) + Fibnum (n-2)

n = int(input())
print (Fibnum(n))
