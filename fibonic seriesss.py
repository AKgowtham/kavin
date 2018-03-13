n=int(input("Enter Fibonacci Range"))
y1 = 0
b1 = 1
count = 0
l=[]
if n == 1:
    l.append(n1)
else:
    while count < n:
        l.append(y1)
        nth = y1 + b1
        y1 = b1
        b1 = nth
        count += 1
print(" ".join(str(x) for x in l))
