n = int(input())

a = [int(i) for i in input().split()]

b = [int(i) for i in input().split()]

a.sort(reverse = True)
b.sort(reverse = True)

sum = 0

for i in range(n):
    sum  += (a[i]*b[i])

print(sum)