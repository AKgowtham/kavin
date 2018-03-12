a=int(input("Enter the size"))
l=list(map(int,input("Enter the values").split(' ')))
for b in l:
    print(b,l.index(b))
