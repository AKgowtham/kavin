def fact(x) :
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                return "no"
        return "yes"
    return "no" 
x = int(input("Enter value"))
print(fact(x))
