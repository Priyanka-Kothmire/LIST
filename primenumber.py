number=[1,2,5,13,24,6,7,10,11,17]
i=0
while i<len(number):
    j=0
    while j<len(number[i]):
        count=0
        if number[j]%i:
            count=count+1
        i=i+1
        if count==0:
            print("prime number")
        else:
            print("not prime number")
