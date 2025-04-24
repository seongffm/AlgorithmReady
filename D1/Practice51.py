#함수의 기초4
# N = int(input())
# n1,n2 = 1,1
# result=[1,1]
# for i in range(3,N+1):
#     N1 = n2
#     N2 = n1+n2
#     n1 = N1
#     n2 = N2
#     result.append(n2)
# print(result)

#파이썬에서는 여러변수에 동시 할당 할 수 있다 ,를 이용해서
#=>
N = int(input())
n1,n2 =1,1
result=[1,1]
for i in range(2,N):
    n1,n2 = n2, n1+n2
    result.append(n2)
print(result)