a=(input('enter'))
b=[]
for i in a:
  count=a.count(i)
if count>=2:
  b.append(i)
if len(b)==2:
  print(b[0])
else:
  continue
    
