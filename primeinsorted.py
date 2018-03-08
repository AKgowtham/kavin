m=int(input())
l=list(1 for i in range(m))
li=[]
for i in range(2,m,1):
    if l[i]==1:
        for j in range(i*i,m,i):
            l[j]=0
        if m%i==0:
            li.append(i)
print(" ".join(str(x) for x in li))
