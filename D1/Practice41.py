#흐름과 제어 - 반복 5
result =0
for i in range(1,101):
    if i%3==0:
        result +=i
print(f"1부터 100사이의 숫자 중 3의 배수의 총합: {result}")