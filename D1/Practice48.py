#내장함수 4
# sentence = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
# score = sentence.count('A')*4 + sentence.count('B')*3+ sentence.count('C')*2+ sentence.count('D')*1
# print(score)

#--> map함수와 람다식을 이용해 구하시오
#map 함수 개념: map(function, iterable)함수
#lambda 함수 개념: 익명 함수 ()
#lambda 함수 정렬할때 key값 지정으로 사용가능 ex) sorted(words, key = lambda x : x[2] #두번째 요소 의미)
#-> words = (1,banana)일때 두번째 요소 기준으로 정렬(문자열)한다는 뜻뜻 
#딕셔너리로 리턴(value값 뱉어냄)

sentence = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
score = map(lambda ch: {'A':4,'B':3,'C':2,'D':1}.get(ch,0), sentence)
print(sum(score))