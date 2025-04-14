#1대1 가위바위보 
a,b= map(int,input().split())
if a ==1 and b==3:
    print("A")
elif a==2 and b==1:
    print("A")
elif a==3 and b==2:
    print("A")
else:
    # if a==b:
    #     print("비김")
    # else:
    #     print("B")
    print("B")