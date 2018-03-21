symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
def check(name):
    k=0
    for i in name:
        if i in symbol:
           k+=1
    return k           
print(check(input("Enter String:")))
