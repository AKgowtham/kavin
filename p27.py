z=list(input("enter"))
for i in range(len(z)):
  if z[i].islower():
    z[i]=z[i].upper()
  else:
    z[i]=z[i].lower()
z="".join(z)
print(z)
