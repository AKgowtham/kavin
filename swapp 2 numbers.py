f,j=map(int,input("Enter Two values").split(' '))
f = f ^ j;
j = f ^ j;
f = f ^ j;
print(f,j)
