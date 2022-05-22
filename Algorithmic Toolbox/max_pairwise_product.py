#Uses python3

def MaxPairwiseProductFast(A,n):
    index1 = 0
    index2 = 0
    
    for i in range(1,n):
        if(A[i]>A[index1]):
            index1 = i
            
    if(index1 == 0):
        index2 = 1 
        
    for i in range(0,n):    
        if((i != index1) and (A[i]>A[index2])):
            index2 = i
            
    return A[index1]*A[index2]
            
 
n = int(input()) 
a = list(map (int, input().split(" "))) 
print(MaxPairwiseProductFast(a,n))
 
 
