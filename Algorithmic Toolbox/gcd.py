def GCDEuc(a,b):
    if(b == 0):
        return a
    else:
        return GCDEuc(b,a%b)
    
 
    
a,b = map(int, input().split())
print(GCDEuc(a,b))