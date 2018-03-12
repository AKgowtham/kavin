n=int(input("Enter the Number"))
v1 = 0
v2 = 1
count = 0
l=[]
if n == 1:
    l.append(n1)
    print(l)
else:
    while count < n:
        l.append(v1)
        nth = v1 + v2
        v1 = v2
        v2 = nth
        count += 1
print(" ".join(str(x) for x in l))
