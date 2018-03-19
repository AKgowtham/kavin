lt=int(input())
fact=0
for i in range(1,nt):
  if lt%i==0:
    fact=i
if fact>1:
  print ('Yes')
elif lt==1:
  print ('neither prime nor composite')
else:
  print ('No')
