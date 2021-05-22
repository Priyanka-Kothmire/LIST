question_list= [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1] 
i=0
while i<len(question_list):   
    print(question_list[i])
    j=0
    k=i
    while j<len(options_list[i]):
        l=options_list[k][j]
        print(j+1,l)
        j=j+1
    answer=int(input("enter the answer"))
    if answer==solution_list[i]:
        print("congratulation")
    else:
        print("wrong")
        break
    i=i+1
    
