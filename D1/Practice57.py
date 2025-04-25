#함수의 기초 7
def factorial(num):
    result=1
    for i in range(num,0,-1):
        result*=i
    # return print(result)
    return result
#이렇게 반환값에 출력문 하는것 보다는
# factorial(int(input()))
#마지막에 출력
print(factorial(int(input())))