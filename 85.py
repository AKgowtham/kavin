s=input("Enter the string")
list1=[]
list2=[]
for k in range(len(s)):
    if k%2==0:list1.append(s[k])
    else:list2.append(s[k])
print("".join(str(x) for x in list1),"".join(str(x) for x in list2))
