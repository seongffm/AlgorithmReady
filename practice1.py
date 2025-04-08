# 1859. 백만 장자 프로젝트
# T= int(input())
# for num in range(1,T+1):
#     N=int(input())
#     price_lst=list(map(int,input().split()))
#     price_max = max(price_lst)
#     cnt=0
#     price_sum=0
#     result=0
#     for i in price_lst:
#         if price_max!=i:
#             cnt+=1
#             price_sum+=i
#         else:
#             if cnt>0:
#                 result+=price_max*cnt-price_sum
#             cnt=0
#             price_sum=0
#     if cnt>0:
#         result+=price_max*cnt-price_sum
#     print(f"#{num} {result}")
# => 오답
# 이렇게 앞에서 접근하면 불확실한 미래(더 큰값이 나온다면 팔지 않아야함)때문에 판단이 어렵고,
#  뒤에서 접근하면 확정된 미래(작으면 팔고, 더 큰값나오면 갱신하고) 기준으로 판단이 명확해짐

T= int(input())
for tc in range(1,T+1):
    N=int(input())
    prices= list(map(int,input().split()))
    prices=prices[::-1]
    max_price = prices[0]
    profit=0
    for price_num in range(N):
        if max_price>prices[price_num]:
            profit+= max_price-prices[price_num]
        else:
            max_price=prices[price_num]
    print(f"#{tc} {profit}")