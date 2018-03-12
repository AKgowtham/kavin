b,m=input("Enter b and m").split(' ')
b,m=int(b),int(m)
a=list(map(int,input("Enter values").split(' ')))
print(sum(a[:m]))
