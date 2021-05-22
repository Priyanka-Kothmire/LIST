mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
b=mainStr.split()
i=0
while i<len(mainStr):
        if "over" in b:
                b.remove("over")
        i=i+1
print(b)
