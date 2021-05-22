char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
b=[]
i=0
while i<len(char_list):
        j=0
        count=0
        k=[]
        while j<len(char_list):
                if char_list[i]==char_list[j]:
                        count=count+1
                j=j+1
        k.append(char_list[i])
        k.append(count)
        if k not in b:
                b.append(k)
        i=i+1
print(b)



