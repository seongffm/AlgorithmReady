#흐름과 제어 - 반복10
num = input()
lst = ['0','1','2','3','4','5','6','7','8','9']
result =[]
for i in lst:
    result.append(num.count(i))
print(*lst)
print(*result)