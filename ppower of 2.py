def isPowerOfTwo(m):
    if (m == 0):return False
    while (m != 1):
        if (m % 2 != 0):return False
        m = m // 2
    return True
m=int(input("Enter Value"))
if(isPowerOfTwo(m)):print('yes')
else:print('no')
