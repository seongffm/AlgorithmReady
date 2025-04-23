#중간값 찾기
N=int(input())
num_lst=list(map(int,input().split()))
medium_idx=N//2 #N이 항상 홀수고 index는 0부터 시작하니까
num_lst.sort()
result=num_lst[medium_idx]
print(result)