#아주 간단한 계산기
a,b = map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print문 하나만 쓰기 ->
# "\n"쓰면 한칸 띄워지니까 sep=''으로 방지지
print(a+b,"\n",a-b,"\n",a*b,"\n",a//b,sep='')