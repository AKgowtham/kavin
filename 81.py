number=int(input("Enter number of lines"))
for i in range(number):
    x,y=map(int,input("Ninja's and kabali's value").split(' '))
    print(abs(x-y))
