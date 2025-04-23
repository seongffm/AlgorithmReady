#함수의 기초3
# import math
# def inspect(num):
#     cnt=0
#     for i in range(1,int(math.sqrt(num))+1):
#         if num%i==0:
#             cnt+=1
#             if i!=(num//i):
#                 cnt+=1
#     if cnt==2:
#         return '소수입니다.'
#     else:
#         return '소수가 아닙니다.'
# print(inspect(int(input())))

#더 명확하고 직관적인 소수 판별코드
import math
def perfect_inspect(num):
    if num<2 :
        return '소수가 아닙니다.'
    for i in range(2,int(math.sqrt(num))+1):
        if num%i ==0:
            return '소수가 아닙니다.'
    return '소수입니다.'
print(perfect_inspect(int(input())))