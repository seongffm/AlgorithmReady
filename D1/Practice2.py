#평균값 구하기
T=int(input())
for tc in range(1,T+1):
    num_lst=list(map(int,input().split()))
    num_sum=sum(num_lst)
    result=round(num_sum/10) #반올림함수수
    print(f"#{tc} {result}")