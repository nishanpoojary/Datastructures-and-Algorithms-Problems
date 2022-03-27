n, W = [int(i) for i in input().split()]

L = []

for _ in range(n):
    v, w = [int(i) for i in input().split()]
    if(v == 0):
        continue
    L.append((v,w))
    
L.sort(key = lambda x: x[0]/x[1], reverse = True)

total = 0
for v,w in L:
    if(W == 0):
        print("{0:.4f}".format(total))
        quit()
    amt = min(w, W)    
    total += amt*(v/w)
    W -= amt

print("{0:.4f}".format(total))