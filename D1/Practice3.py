#큰 놈, 작은 놈, 같은 놈
T=int(input())
for tc in range(1,T+1):
    n1,n2=map(int,input().split())
    result=""
    if n1==n2:
        result="="
    elif n1>n2:
        result=">"
    else:
        result="<"
    print(f"#{tc} {result}")
