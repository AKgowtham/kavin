p=list(input())
m1=[]
for x1 in p:
    if x1.isdigit():
        m1.append(x1)
print("".join(str(n) for n in m1))
