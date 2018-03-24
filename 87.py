k1,j1=map(int,input().split(' '))
if k1 > j1:
    smaller = j1
else:
    smaller = k1
for i in range(1, smaller+1):
    if((k1 % i == 0) and (j1 % i == 0)):abd1 = i
print(abd1)
