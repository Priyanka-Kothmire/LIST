a=[50, 40, 23, 70, 56, 12, 5, 10, 7, 33, 28, 38]
i=0
count=0
while i<len(a):
    #print(a[i])
    if a[i]>20 and a[i]<40:
        count=count+1
    i=i+1
print(count)