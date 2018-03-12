c,a=input().split()
c,a=int(c),int(a)
l=[]
for num in range(c+1,a):

   order = len(str(num))

   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       l.append(num)
print(" ".join(str(x) for x in l))
