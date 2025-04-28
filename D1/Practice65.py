#내장함수 7
lst = [1,2,3,4,5,6,7,8,9,10]
#리스트에서 조건을 만족하는 요소만 골라내는 함수 :filter() 
result = list(filter(lambda x: x%2 ==0,lst))
print(result)