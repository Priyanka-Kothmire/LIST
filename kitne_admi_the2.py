elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
sum=0
average=0
even=[]
odd=[]
i=0
while i<len(elements):
    if elements[i] %2==0:
        sum=sum+elements[i]
        average=sum//elements[i]
        even.append(elements[i])
    else:
        sum=sum+elements[i]
        average=sum//elements[i]
        odd.append(elements[i])
    i=i+1
print("even elements",even,"total sum",sum,"average",average)
print("odd elements",odd,"total sum",sum,"average",average)
