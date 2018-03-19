h=['a','e','i','o','u','A','E','I','O','U']
def hm(s):
    for i in h:
        if i in s:
            return "yes"
    return "no"
s=list(input("Enter the string"))
print(hm(s))
