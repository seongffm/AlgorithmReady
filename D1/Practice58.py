#내장함수 5
# input_1 = "1, 2, '4', 3"
# lst = list(map(str,input_1.split(', ')))
# result=1
# for i in lst:
#     if "'" in i or '"' in i :
#         result = '에러발생'
#         break
#     else:
#          result*=int(i)
# print(result)

#개선코드
input_1 = '1, 2, \'4\', 3'
lst = input_1.split(', ')
result = 1
try:
    for i in lst:
        if "'" in i or '"' in i:
            raise ValueError('문자열이 포함됨')
        result *= int(i)
    print(result)
except:
    print('에러발생')