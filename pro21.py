a=int(input("enter"))
b=[]
for i in range(0,a):
  c=int(input("enter the list"))
  b.append(c)
print(b) 
am=b[len(b)//2:]
an=b[:len(b)//2]
m=sum(am)/len(am)
n=sum(an)/len(an)
if m==n:
  print('yes')
else:
  print('no')  
