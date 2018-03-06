n=int(input("enter the number"))
sum=0
while(n>0):
  s=n%10
  sum=sum+s
  n=n//10
print(sum)
