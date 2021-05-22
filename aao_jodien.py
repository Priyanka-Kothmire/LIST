elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
sum=0
sum1=0
i=0
even=[]
odd=[]
while i<len(elements):
    if elements[i] %2==0:
        k=elements[i]
        print(k)
        sum=sum+elements[i]
        even.append(elements[i])
        sum=sum+elements[i]
        print("even elements:",sum)
    else:
        sum=sum+elements[i]
        odd.append(elements[i])
        print("even elements :",sum)
        odd.append(elements[i])
        sum1=sum1+elements[i]
    i=i+1
print("even elements :",even,"total:",sum)
print("odd elements :",odd,"total",sum1)










