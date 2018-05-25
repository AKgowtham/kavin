a=input("het")
a=a.split()
c=[]
for i in a:
  c.append(i[::-1])
print(" ".join(c)) 
