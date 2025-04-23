# #흐름과 제어 - if 8
# for i in range(100,301):
#     num = 0
#     for j in str(i):
#         if int(j)%2==0:
#             num +=1
#     if num ==3 :
#         print(i,end=',') #마지막, 출력하기 싫은데
# print()

#=> 해결 방법
result = []
for i in range(100,301):
    num = 0
    for j in str(i):
        if int(j)%2==0:
            num+=1
    if num ==3:
        result.append(str(i))
print(','.join(result))

# #형변환 최소화
# result = []
# for i in range(100,301):
#     digits = [i//100,(i//10)%10,i%10]
#     # 리스트 컴프리헨션 말고 바로 제너레이터로 만들어 메모리절약
#     even_count = sum(1 for d in digits if d%2 == 0)
#     if even_count==3:
#         result.append(str(i))
# print(*result) #[]만 벗겨서 출력(공백으로 구분)
# print(','.join(result)) #(문자열 리스트만 가능)