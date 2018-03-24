h1,y1=map(int,input().split(' '))
if h1 > y1:
    great = h1
else:
    great = y1
while(True):
    if((great % h1 == 0) and (great % y1 == 0)):
        jpm = great
        break
    great += 1
print(jpm)
