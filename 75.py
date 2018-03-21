sk=input()
if(len(sk)%2==0):
    sk=sk[:int((len(sk)/2))-1]+'**'+sk[int(len(sk)/2)+1:]
else:
    sk=sk[:int(len(sk)/2)]+'*'+sk[int(len(sk)/2)+1:]
print(sk)
