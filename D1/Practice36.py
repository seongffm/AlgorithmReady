#흐름과 제어 - 반복 3
result =[]
for i in range(1,101):
    if i%2==0:
        result.append(i)
print(*result)