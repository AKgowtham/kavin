M1,y1=map(int,input("Enter 1st line").split(' '))
M2,y2=map(int,input("Enter 2nd line").split(' '))
M3,y3=map(int,input("Enter 3rd line").split(' '))
if (M1==M2 and M2==x3) or(y1==y2 and y2==y3) or (abs(M1-M2)==abs(M2-M3) and abs(y1-y2)==abs(y2-y3)): 
  print("yes")
else:
  print("no")
