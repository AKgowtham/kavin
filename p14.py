def conso(text):
        for i in "aeiouAEIOU":
            text = text.replace(i,"")
        return text[::-1]
print(conso(input("enter text:")))
