#흐름과 제어 -if 2
N = int(input())
cnt=[]
for i in range(1,N+1):
    if N%i == 0:
        print(f"{i}(은)는 {N}의 약수입니다.")
        cnt.append(i)
if len(cnt) ==2:
    print(f"{N}(은)는 {cnt[0]}과 {cnt[1]}로만 나눌 수 있는 소수입니다.")

#약수 판별(시간복잡도 줄이는 방법)
#아이디어 -> 약수는 항상 짝을 가지고 있다 -> 제곱근 까지만 판별 sqrt()이용
# import math
# N = int(input())
# cnt =[]
# for i in range(1, int(math.sqrt(N))+1):
#     if N%i ==0:
#         cnt.append(i)
#         if i!=N//i:
#             cnt.append(N//i)
# cnt.sort()
# for divisor in cnt:
#     print(f"약수{divisor}")
# if len(cnt)==2:
#     print(f"{N}은 소수이며 {cnt[0]},{cnt[1]}의 약수 가지고 있음")