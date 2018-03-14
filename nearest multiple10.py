x2=int(input("Enter Value"))
if x2<10: print("10")
else:
    m2=len(str(x2))
    x2+=5
    x2=x2/(10**(m2-1))
    print(math.floor(x2)*(10**(m2-1)))
