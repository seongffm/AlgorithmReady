#최대수 구하기기
T=int(input())
for tc in range(1,T+1):
    num_lst = list(map(int,input().split()))
    num_lst.sort(reverse=True)
    result=num_lst[0]
    print(f"#{tc} {result}")