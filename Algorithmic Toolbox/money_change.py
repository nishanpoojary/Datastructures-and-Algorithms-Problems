n = int(input())

sum = 0

tens =  n//10
sum = 10*tens

fives = (n - sum)//5
sum = sum + (5*fives)

ones = n - sum

print(tens+fives+ones)