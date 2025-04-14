#서랍의 비밀번호 
p,k = map(int,input().split())
#비밀번호 p는 0~999
#주어지는 번호 k= 1부터 증가시켜 비밀번호 확인
if p>=k:
    cnt = p-k+1
else:
    # 999까지 돌리고 0부터 다시 시작작
    1000-k+p+1
print(cnt)