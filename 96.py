m = int(input("Enter any number : "))
if m> 1:
    for i in range(2, m):
        if (m % i) == 0:
            print("Yes")
            break
    else:
        print("No")
elif m == 0 or 1:
    print(" a neither prime NOR composite number")
else:
    print("Yes")
