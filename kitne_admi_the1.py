elements = [1,2,3,4,5,6,7,8,9,1] 
sum=0
i=0
even=[]
odd=[]
while i<len(elements):
    if elements[i] %2==0:
        k=elements[i]
        print(k,even)
        sum=sum+elements[i]
        even.append(elements[i])
        print("even elements:",even)
    else:
        sum=sum+elements[i]
        odd.append(elements[i])
        print("even elements :",odd)
    i=i+1
print("even elements :",even,"total:",sum)
print("odd elements :",odd,"total",sum)
