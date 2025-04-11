#홀수만 더하기
T=int(input())
for i in range(1,T+1):
    num_lst=list(map(int,input().split()))
    result=0
    for j in num_lst:
        if j%2!=0:
            result+=j
    print(f"#{i} {result}")
    