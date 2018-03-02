p=int(input())
rev=0
while(p>0):
    dig=p%10
    rev=rev*10+dig
    p=p//10
print(rev)
