a1,m1=input("Enter first time").split()
a1,m1=int(a1),int(m1)
b3,m2=input("Enter Second time").split()
b3,m2=int(b3),int(m2)
l1=(a1*60)+m1
l2= (b3*60)+m2
tmin=abs(l1-l2)
h = tmin  % 60
hrs = (tmin - h) / 60
print (int(hrs),int(h))
