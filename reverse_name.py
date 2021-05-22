places=input("enter the name")
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
a=[ ]
length=len(places)
print(length)
i=1
while i<=len(places):
    a.append(places[-i])
    a=places[-i]
    i=i+1
print(places)
print(a)



