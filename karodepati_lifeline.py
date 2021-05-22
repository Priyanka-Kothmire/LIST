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
ans="1.four","3.seven" "1.chandigarh","4.delhi""3.tourism","1.Software Engineering" 
i=0
r=1
y=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    k=i
    while j<len(options_list[i]):
        l=(options_list[k][j])
        print(j+1,l)
        j=j+1
    lifeline=input("Do you want 5050 lifeline :")
    if lifeline=="yes":
        # print("5050")
        if count==0:
            print(ans[y+i])
            print(ans[y+r])
            n=int(input("enter the answer :"))
            if n==solution_list[i]:
                print("right answer")
            else:
                print("sorry,lost")
                break
            count=count+1
        else:
            print("you already used lifeline")
            m=int(input("enter the answer :"))
            if m==solution_list[i]:
                print("your answer is right")
            else:
                print("your lost")
    elif lifeline=="no":
        u=int(input("choose the answer :"))
        if u==solution_list[i]:
            print("congratualtion,your win")
        else:
             print("Sorry,your lost")
             break
    else:
        ("error")
    i=i+1
    r=r+1
    y=y+1


