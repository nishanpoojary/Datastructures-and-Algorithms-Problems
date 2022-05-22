def GCDEuc(a,b):
    if(b == 0):
        return a
    else:
        return GCDEuc(b,a%b)
        
a,b = map(int, input().split())

if(a>b):
    gcd = GCDEuc(a,b)
else:
    gcd = GCDEuc(b,a)
    
print((a*b)//gcd)
    