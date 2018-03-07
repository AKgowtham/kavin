tmin = int(input("Enter time in minutes"))
n= tmin  % 60
hrs = (tmin - n) / 60
print (int(hrs),int(n))
